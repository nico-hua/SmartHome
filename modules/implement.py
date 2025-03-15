from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from utils.logger import Logger
from utils.device_api import light, tv, audio_player, air_conditioner, curtain

class ImplementModule:
    def __init__(self):
        self.logger = Logger()
        self.llm = ChatTongyi(model="qwen-plus", temperature=0.1)  # 使用 ChatTongyi 的 qwen-plus
        self.implement_prompt = PromptTemplate(
            input_variables=["task_plan", "device_apis"],
            template="""
            You are a smart home AI assistant. Your task is to generate executable Python code based on a task plan and the API descriptions of available devices.
            Follow these rules:
            1. Analyze the task plan and the device API descriptions.
            2. Generate Python code that implements the task plan using the provided APIs.
            3. Ensure the code is complete and executable.

            Examples:
            - Task Plan:
              1. Turn off the lights.
              2. Turn on the TV.
              3. Set the audio_player volume to 50%.
              Device APIs:
              light: "light.set_brightness(brightness: int)"
              tv: "tv.set_power(status: bool)"
              audio_player: "audio_player.set_volume(volume: int)"
              Python Code:
              ```python
              light.set_brightness(0)
              tv.set_power(True)
              audio_player.set_volume(50)
              ```

            - Task Plan:
              1. Set the air conditioner temperature to 26°C.
              Device APIs:
              air_conditioner: "air_conditioner.set_temperature(temperature: int)"
              Python Code:
              ```python
              air_conditioner.set_temperature(26)
              ```

            Task Plan:
            {task_plan}
            Device APIs:
            {device_apis}
            Python Code:
            """
        )
        self.chain = self.implement_prompt | self.llm

    def generate_code(self, task_plan, device_apis):
        """
        生成可执行的 Python 代码。
        :param task_plan: 任务计划（List[str]），例如 ["1. Turn off the lights.", "2. Turn on the TV."]
        :param device_apis: 设备 API 描述（字典格式，例如 {"light": "light.set_brightness(brightness: int)"}）
        :return: 生成的 Python 代码（字符串），如果出错则返回空字符串
        """
        try:
            # Step 1: 将任务计划和设备 API 描述转换为字符串
            task_plan_str = "\n".join(task_plan)
            device_apis_str = "\n".join([f"{device}: {api}" for device, api in device_apis.items()])

            # Step 2: 调用 LLM 生成 Python 代码
            response = self.chain.invoke({
                "task_plan": task_plan_str,
                "device_apis": device_apis_str
            }).content
            self.logger.log(f"Implement Module:\n{response}")

            # Step 3: 提取生成的 Python 代码
            # 假设 LLM 返回的代码包含在 ```python ``` 标记中
            if "```python" in response:
                code = response.split("```python")[1].split("```")[0].strip()
            else:
                code = response.strip()
            return code
        except Exception as e:
            self.logger.log(f"Code Generation Error: {str(e)}", level="ERROR")
            return ""  # 如果出错，返回空字符串
        
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
            print("代码执行成功！")
        except Exception as e:
            print(f"代码执行失败: {str(e)}")