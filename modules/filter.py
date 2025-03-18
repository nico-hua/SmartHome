from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
from utils.redis_util import RedisUtils
from tools.rag import RAGModule
import json

class FilterModule:
    def __init__(self, available_devices, uuid, instruction):
        """
        初始化 Filter 模块。
        :param available_devices: 家庭中已有的物理设备类型列表，例如 ["air_conditioner", "light", "tv", "audio_player", "curtain"]
        :param uuid: 流程的标识
        :param instruction: 用户的指令（经 clarification 处理）
        """
        self.logger = Logger()
        self.redis = RedisUtils()
        self.rag = RAGModule()
        self.uuid = uuid
        self.instruction = instruction
        self.llm = ChatTongyi(model="qwen-turbo", temperature=0.1)  # 使用 ChatTongyi 的 LLM
        self.available_devices = available_devices

    def filter_devices(self):
        """
        过滤出完成用户指令可能需要的物理设备类型。
        :param instruction: 用户的指令（经过 Clarify 模块处理后的规范化指令）
        :return: JSON 格式的结果，包含设备列表
        """
        try:
            # Step 1: 使用rag检索相似指令的指令和执行结果
            similar_instruction_info = self.rag.get_similar_instruction_info(self.instruction)
            prompt_template = self.genarate_prompt(similar_instruction_info)
            # Step 2: 调用 LLM 进行设备过滤
            filter_prompt = PromptTemplate(
                input_variables=["instruction", "available_devices"],
                template=prompt_template
            )
            chain = filter_prompt | self.llm
            response = chain.invoke({
                "instruction": self.instruction,
                "available_devices": ", ".join(self.available_devices)
            }).content
            self.logger.log(f"Filter Module:\n{response}")
            # 打印原始响应内容以进行调试
            # Step 3: 解析 LLM 的响应并生成 JSON
            if isinstance(response, (list, dict)):
                devices = response
            else:
                devices = json.loads(response)
            self.logger.log(f"Parsed Devices: {devices}")
            # Step 4: 将结果存储到redis
            key = f"Filter:{self.uuid}"
            self.redis.set_value(key, response)
            return json.dumps({
                "status": "success",
                "devices": devices
            }, ensure_ascii=False)
        except Exception as e:
            self.logger.log(f"Filter Error: {str(e)}", level="ERROR")
            return json.dumps({
                "status": "error",
                "reason": "系统出现错误，请稍后再试。"
            }, ensure_ascii=False)
    
    def genarate_prompt(self, similar_instructions_info):
        """
        动态生成提示词模板
        """
        prompt_template = """
        You are a smart home AI assistant. Your task is to determine which physical devices are needed to execute a user instruction.
        Follow these rules:
        1. Analyze the user instruction and identify the types of devices required.
        2. Only return devices that are in the available devices list.
        3. If no devices are needed, return an empty list.

        Available devices: {available_devices}

        Examples:
        - Instruction: "用户需要打开客厅的空调"
          ["air_conditioner"]
        - Instruction: "用户需要调亮卧室的灯光"
          ["light"]
        - Instruction: "用户需要开启电影之夜模式"
          ["light", "tv", "audio_player"]
        - Instruction: "用户需要调整灯光、音乐和温度等设备来准备派对。"
          ["light", "audio_player", "air_conditioner"] 
        """
        # 加入相似指令执行信息
        if similar_instructions_info is not None:
            similar_instructions_info = json.loads(similar_instructions_info)
            prompt_template += f"""
            Similar instructions and their feedback:
            - Instruction: {similar_instructions_info['instruction']}
            {similar_instructions_info['devices']}
            """
            if similar_instructions_info['feedback']['status'] == 'unsatisfied':
                prompt_template += f"""
                Feedback: User was not satisfied with the previous execution. Special attention is needed.
                Feedback details: {similar_instructions_info['feedback']['feedback']}        
                """
            else:
                prompt_template += f"""
                Feedback: User was satisfied with the previous execution.
                """
        prompt_template += """
        Instruction: {instruction}
        """
        return prompt_template
