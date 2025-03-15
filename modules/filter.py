from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
import json

class FilterModule:
    def __init__(self, available_devices):
        """
        初始化 Filter 模块。
        :param available_devices: 家庭中已有的物理设备类型列表，例如 ["air_conditioner", "light", "tv", "audio_player", "curtain"]
        """
        self.logger = Logger()
        self.llm = ChatTongyi(model="qwen-turbo", temperature=0.1)  # 使用 ChatTongyi 的 LLM
        self.available_devices = available_devices
        self.filter_prompt = PromptTemplate(
            input_variables=["instruction", "available_devices"],
            template="""
            You are a smart home AI assistant. Your task is to determine which physical devices are needed to execute a user instruction.
            Follow these rules:
            1. Analyze the user instruction and identify the types of devices required.
            2. Only return devices that are in the available devices list.
            3. If no devices are needed, return an empty list.

            Available devices: {available_devices}

            Examples:
            - Instruction: "用户需要打开客厅的空调"
              Devices:
              ["air_conditioner"]
            - Instruction: "用户需要调亮卧室的灯光"
              Devices:
              ["light"]
            - Instruction: "用户需要开启电影之夜模式"
              Devices:
              ["light", "tv", "audio_player"]
            - Instruction: "用户需要调整灯光、音乐和温度等设备来准备派对。"
              Devices:
              ["light", "audio_player", "air_conditioner"]

            Instruction: {instruction}
            Devices:
            """
        )
        self.chain = self.filter_prompt | self.llm

    def filter_devices(self, instruction):
        """
        过滤出完成用户指令可能需要的物理设备类型。
        :param instruction: 用户的指令（经过 Clarify 模块处理后的规范化指令）
        :return: JSON 格式的结果，包含设备列表
        """
        try:
            # Step 1: 调用 LLM 进行设备过滤
            response = self.chain.invoke({
                "instruction": instruction,
                "available_devices": ", ".join(self.available_devices)
            }).content
            self.logger.log(f"Filter Module:\n{response}")

            # Step 2: 解析 LLM 的响应并生成 JSON
            devices = json.loads(response)
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