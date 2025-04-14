from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
from utils.redis_util import RedisUtils
from tools.rag import RAGModule
import json
import os

class PlanModule:
    def __init__(self, device_info_path="../config/device_info.json"):
        """"
        初始化 PlanModule 模块
        :param device_info_path: 设备描述信息路径
        """
        self.logger = Logger()
        self.redis = RedisUtils()
        self.rag = RAGModule()
        self.device_info = self.get_device_info(device_info_path)
        self.llm = ChatTongyi(model="qwen-plus", temperature=0.1)

    def get_device_info(self, device_info_path):
        """
        读取device_info.json文件
        """
        try:
            # 获取当前文件的绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 构建配置文件的绝对路径
            abs_config_path = os.path.join(current_dir, device_info_path)
            with open(abs_config_path, "r", encoding='utf-8') as f:
                device_info = json.load(f)
            return device_info
        except FileNotFoundError:
                raise Exception(f"配置文件 {device_info_path} 未找到")
        except json.JSONDecodeError:
            raise Exception("配置文件格式错误")
        except Exception as e:
            raise Exception(f"报错: {str(e)}")
    
    def generate_plan(self, uuid, instruction, recommend_devices, location):
        """
        生成可执行的计划
        :param uuid: 唯一标识符
        :param instruction: 用户指令
        :param recommend_devices: 推荐的设备列表
        :param location: 用户所在的房间
        """
        # Step 1:从推荐的设备列表中过滤出设备信息
        filtered_device_info = self.filter_device_info(recommend_devices)
        filtered_device_info_str = "\n".join( [f"{device_type}:\n" + "\n".join(functions) for device_type, functions in filtered_device_info.items()])
        # Step 2:构建提示词模板
        prompt_template = PromptTemplate(
            input_variables=["instruction", "device_info","location"],
            template=
            """
            You are a smart home AI assistant. Your task is to generate an executable plan based on the user's instruction and the available device functions. 
            The plan should be a step-by-step guide, where each step corresponds to a specific device function.

            User Instruction: {instruction}

            Available Device Functions:
            {device_info}

            Additional Information:
            - The user is currently in the {location}.
            - If the user's instruction does not specify a room, assume the devices are in the {location}.
            - In the generated plan, each step must explicitly mention the room where the device is located (e.g., "Turn on the light in the living room").

            Please generate a plan in the following format:
            1. [Step 1]: [Device Function in Room]
            2. [Step 2]: [Device Function in Room]
            ...

            Example:
            1. Turn on the light in the living room.
            2. Set the air conditioner in the bedroom to cooling mode.
            3. Close the curtains in the living room.

            Now, generate a plan for the user:
            """
        )
        # Step 3:调用LLM生成计划
        chain = prompt_template | self.llm
        response = chain.invoke({
            "instruction": instruction,
            "device_info": filtered_device_info_str,
            "location": location
        }).content
        self.logger.log(f"Plan Module:生成的可执行计划\n{response}")
        # Step 4: 返回任务计划
        return response
    
    def filter_device_info(self, recommend_devices):
        """
        过滤设备信息
        :param recommend_devices: 推荐的设备列表
        """
        filtered_device_info = {}
        for device in recommend_devices:
            device_type = device.get("type")
            if device_type in self.device_info:
                filtered_device_info[device_type] = self.device_info[device_type]
        return filtered_device_info
    

        
