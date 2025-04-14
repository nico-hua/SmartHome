from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
from utils.device_api import light, tv, audio_player, air_conditioner, curtain
from utils.redis_util import RedisUtils
import os
import json

class ImplementModule:
    def __init__(self, device_api_info_path="../config/device_api_info.json"):
        """
        初始化 ImplementModule 模块
        :param device_api_info_path: 设备 API 信息路径
        """
        self.logger = Logger()
        self.redis = RedisUtils()
        self.device_api_info = self.get_device_api_info(device_api_info_path)
        self.llm = ChatTongyi(model="qwen-plus", temperature=0.1)

    def get_device_api_info(self, device_api_info_path):
        """
        读取device_api_info.json文件
        """
        try:
            # 获取当前文件的绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 构建配置文件的绝对路径
            abs_config_path = os.path.join(current_dir, device_api_info_path)
            with open(abs_config_path, "r", encoding='utf-8') as f:
                device_info = json.load(f)
            return device_info
        except FileNotFoundError:
                raise Exception(f"配置文件 {device_api_info_path} 未找到")
        except json.JSONDecodeError:
            raise Exception("配置文件格式错误")
        except Exception as e:
            raise Exception(f"报错: {str(e)}")
    
    def generate_code(self, uuid, plan, recommend_devices):
        """
        生成可执行的 Python 代码
        :param uuid: 唯一标识符
        :param plan: 计划
        :param recommend_devices: 推荐的设备列表
        :return: 生成的 Python 代码
        """
        # Step 1: 从推荐的设备列表中过滤出设备 API 信息
        filtered_device_api_info = self.filter_device_api_info(recommend_devices)
        device_api_info_str = json.dumps(filtered_device_api_info, ensure_ascii=False, indent=2)
        device_info_str = json.dumps(recommend_devices, ensure_ascii=False, indent=2)
        # Step 2: 构建提示词
        prompt = PromptTemplate(
            input_variables=["plan", "device_api_info", "device_info"],
            template=
            """
            You are a smart home AI assistant. Your task is to generate executable Python code based on the following information:

            Execution Plan:
            {plan}

            Available Device APIs:
            {device_api_info}

            Device information including device ID:
            {device_info}

            Additional Information:
            1. The device ID is constructed as "devicetype_roomname" (e.g., "light_living_room"), so you can infer from the device ID which room it is located in and what type of device it is.

            Requirements:
            1. The code should implement the execution plan step by step.
            2. Each step should use the appropriate device API.

            Example:
            ```python
            # Step 1: Turn on the light in the living room
            light.turn_on("light_living_room")
            # Step 2: Set the TV channel to 5 in the living room
            tv.set_channel("tv_living_room", 5)
            ```

            Now, generate the Python code:
            """
        )
        # Step 2: 调用 LLM 生成 Python 代码
        chain = prompt | self.llm
        response = chain.invoke({
            "plan": plan,
            "device_api_info": device_api_info_str,
            "device_info": device_info_str
        }).content
        self.logger.log(f"Implement Module:生成的代码\n{response}")
        # Step 3: 提取生成的 Python 代码
        # 假设 LLM 返回的代码包含在 ```python ``` 标记中
        if "```python" in response:
            code = response.split("```python")[1].split("```")[0].strip()
        else:
            code = response.strip()
        return code

    def filter_device_api_info(self, recommend_devices):
        """
        过滤设备信息
        :param recommend_devices: 推荐的设备列表
        """
        filtered_device_api_info = {}
        for device in recommend_devices:
            device_type = device.get("type")
            if device_type in self.device_api_info:
                filtered_device_api_info[device_type] = self.device_api_info[device_type]
        return filtered_device_api_info

    def execute_code(self, code):
        """
        执行生成的 Python 代码。
        :param code: 生成的 Python 代码（字符串）
        """
        try:
            # 将设备对象注入到 exec 的执行环境中
            device_objects = {
                "light": light,
                "tv": tv,
                "audio_player": audio_player,
                "air_conditioner": air_conditioner,
                "curtain": curtain
            }
            exec(code, device_objects)
            self.logger.log(f"Code Execution Successful")
            return "SUCCESS"
        except Exception as e:
            self.logger.log(f"Code Execution Error: {str(e)}", level="ERROR")
            return f"执行失败: {str(e)}"