from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
import json

class ClarifyModule:
    def __init__(self):
        self.logger = Logger()
        self.llm = ChatTongyi(model="qwen-turbo", temperature=0.1)  # 使用 ChatTongyi 的 LLM
        self.clarify_prompt = PromptTemplate(
            input_variables=["user_input", "context"],
            template="""
            You are a smart home AI assistant that can complete user instructions with the help of home devices. Your task is to evaluate user instructions.
            Follow these rules:
            1. If the instruction is clear, executable, and contains all necessary information, respond with "SUCCESS: <normalized instruction>".
            2. If the instruction involves context (e.g., previous interactions), you may need combine the context to summarize it into a clear and complete instruction.
            3. If the instruction is unclear or missing details, ask the user for clarification by providing a question, and respond with "NEED_CLARIFY: <question>".
            4. If the instruction is not executable (e.g., due to lack of devices or invalid request), respond with "FAILURE: <reason>".

            Examples:
            example 1:
            - User: "打开客厅的空调"
            - AI: "SUCCESS: 用户需要打开客厅的空调"
            example 2:
            - User: "灯太暗了"
            - AI: "NEED_CLARIFY: 请问您需要调节客厅的灯光还是卧室的灯光？"
            - User: "客厅的" (上下文: 用户之前提到“灯太暗了”)
            - AI: "SUCCESS: 用户需要调亮客厅的灯光"
            example 3:
            - User: "让房子飞起来"
            - AI: "FAILURE: 该指令不可执行，因为没有支持飞行的设备。"

            Context (previous interactions):
            {context}

            Instruction: {user_input}
            """
        )
        self.chain = self.clarify_prompt | self.llm
        self.context = []  # 用于存储对话上下文

    def clarify(self, user_input):
        """
        澄清用户指令，返回 JSON 格式的结果。
        """
        try:
            # Step 1: 构建上下文
            context_str = "\n".join(self.context) if self.context else "no context"

            # Step 2: 调用 LLM 进行指令澄清
            response = self.chain.invoke({"user_input": user_input, "context": context_str}).content
            self.logger.log(f"LLM Response: {response}")

            # Step 3: 解析 LLM 的响应并生成 JSON
            if response.startswith("SUCCESS:"):
                # 指令明确且可执行
                clarified_instruction = response.replace("SUCCESS:", "").strip()
                return json.dumps({
                    "status": "success",
                    "instruction": clarified_instruction
                }, ensure_ascii=False)
            elif response.startswith("NEED_CLARIFY:"):
                # 指令不明确，需要进一步澄清
                clarify_reason = response.replace("NEED_CLARIFY:", "").strip()
                return json.dumps({
                    "status": "need_clarify",
                    "reason": clarify_reason
                }, ensure_ascii=False)
            elif response.startswith("FAILURE:"):
                # 指令不可执行
                failure_reason = response.replace("FAILURE:", "").strip()
                return json.dumps({
                    "status": "failure",
                    "reason": failure_reason
                }, ensure_ascii=False)
            else:
                # 未知响应类型
                return json.dumps({
                    "status": "error",
                    "reason": "未知的 LLM 响应格式。"
                }, ensure_ascii=False)
        except Exception as e:
            self.logger.log(f"Clarification Error: {str(e)}", level="ERROR")
            return json.dumps({
                "status": "error",
                "reason": "系统出现错误，请稍后再试。"
            }, ensure_ascii=False)

    def interact_with_user(self, user_input):
        """
        与用户交互，直到生成一条清晰的指令。
        """
        while True:
            
            # Step 1: 调用 clarify 方法
            result = self.clarify(user_input)
            result_dict = json.loads(result)

            # Step 2: 记录用户指令
            self.context.append(f"User: {user_input}")

            # Step 3: 如果指令明确或不可执行，返回结果
            if result_dict["status"] in ["success", "failure", "error"]:
                return result
            
            # Step 4: 记录LLM回复
            self.context.append(f"AI: {result_dict['reason']}")

            # Step 5: 指令不明确，提示用户输入补充信息
            print(result_dict["reason"])  # 打印 LLM 的澄清问题
            user_input = input("您的回答: ")  # 获取用户补充信息