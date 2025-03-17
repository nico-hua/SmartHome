from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
from utils.redis_util import RedisUtils

class PlanModule:
    def __init__(self, uuid):
        self.logger = Logger()
        self.redis = RedisUtils()
        self.uuid = uuid
        self.llm = ChatTongyi(model="qwen-plus", temperature=0.1)  # 使用 ChatTongyi 的 qwen-plus
        self.plan_prompt = PromptTemplate(
            input_variables=["instruction", "device_descriptions"],
            template="""
            You are a smart home AI assistant. Your task is to generate an executable plan based on a user instruction and the descriptions of available devices.
            Follow these rules:
            1. Analyze the user instruction and the device descriptions.
            2. Break down the instruction into clear and executable steps.
            3. Each step should describe a specific action to be performed by a device.

            Examples:
            - Instruction: "用户需要开启电影之夜模式"
              Device Descriptions: "light: controls the brightness of lights, tv: turns the TV on/off, audio_player: controls audio output"
              Plan:
              1. Turn off the lights.
              2. Turn on the TV.
              3. Set the audio_player volume to 50%.

            - Instruction: "用户需要调高卧室的温度。"
              Device Descriptions: "air_conditioner: controls the temperature of the room"
              Plan:
              1. Increase the air conditioner temperature by 2°C.

            Instruction: {instruction}
            Device Descriptions:
            {device_descriptions}
            Plan:
            """
        )
        self.chain = self.plan_prompt | self.llm

    def generate_plan(self, instruction, device_descriptions):
        """
        生成可执行的任务计划。
        :param instruction: 用户的指令（经过 Clarify 模块处理后的规范化指令）
        :param device_descriptions: 设备描述（字典格式，例如 {"light": "controls the brightness of lights", "tv": "turns the TV on/off"}）
        :return: 可执行的任务计划（List[str]），如果出错则返回空列表
        """
        try:
            # Step 1: 将设备描述转换为字符串
            device_descriptions_str = "\n".join([f"{device}: {desc}" for device, desc in device_descriptions.items()])

            # Step 2: 调用 LLM 生成任务计划
            response = self.chain.invoke({
                "instruction": instruction,
                "device_descriptions": device_descriptions_str
            }).content
            self.logger.log(f"Plan Module:\n{response}")

            # Step 3: 解析 LLM 的响应并返回任务计划
            plan = response.strip().split("\n")  # 假设 LLM 返回的是多行文本，每行是一个步骤
            # Step 4: 将任务计划存储到 redis
            key = f"Plan:{self.uuid}"
            self.redis.set_value(key, plan)
            return plan
        except Exception as e:
            self.logger.log(f"Plan Generation Error: {str(e)}", level="ERROR")
            return []  # 如果出错，返回空列表