from utils.logger import Logger
from utils.redis_util import RedisUtils
from tools.rag import RAGModule
from langchain_community.chat_models import ChatTongyi
from langchain.prompts import PromptTemplate
import json
import os

class FirstModule:
    def __init__(self, uuid, home_info_path, location):
        self.logger = Logger()
        self.redis = RedisUtils()
        self.rag = RAGModule()
        self.uuid = uuid
        self.home_info = self.get_home_info(home_info_path)
        self.llm = ChatTongyi(model="qwen-plus", temperature=0.1)
        self.location = location
    
    def extract_rooms_from_instruction(self, instruction):
        """
        使用大模型从用户指令中提取房间位置信息
        """
        # Step 1:构建提示词模板
        prompt_template = PromptTemplate(
            input_variables=["instruction", "room_names"],
            template = 
            """
            You are a smart home AI assistant. Your task is to extract the room names mentioned in the user's instruction.
            Follow these rules:
            1. Analyze the user's instruction and identify any room names mentioned.
            2. Standardize the room names to match the names in the provided room list.
            3. If no room is mentioned, return an empty list.

            Available room names:
            {room_names}

            Examples:
            - Instruction: "打开客厅的灯"
            Response: ["living_room"]
            - Instruction: "把卧室和厨房的灯都打开"
            Response: ["master_bedroom", "kitchen"]
            - Instruction: "调亮浴室的灯光"
            Response: ["bathroom"]
            - Instruction: "把灯关掉"
            Response: []

            Instruction: {instruction}

            Response format:
            [ "<room_name>", ... ]

            Note: Only return room names from the provided list, no additional information.
            """
        )
        # Step 2: 从家庭布局信息中提取房间名称
        room_names = self.extract_rooms_from_home_info()
        # 调用大模型提取房间名称
        chain = prompt_template | self.llm
        response = chain.invoke({
            "instruction": instruction,
            "room_names": room_names
        }).content
        # Step 3: 解析大模型的响应
        try:
            mentioned_rooms = json.loads(response)
            if isinstance(mentioned_rooms, list):
                # 确保提取的房间名称在标准房间名称列表中
                mentioned_rooms = [room for room in mentioned_rooms if room in room_names]
                self.logger.log(f"First Module:\n{mentioned_rooms}")
                return mentioned_rooms
            else:
                raise ValueError("Invalid response format from LLM.")
        except json.JSONDecodeError:
            # 如果响应不是 JSON 格式，尝试手动解析
            if response.startswith("[") and response.endswith("]"):
                mentioned_rooms = response[1:-1].split(",")
                mentioned_rooms = [room.strip().strip('"') for room in mentioned_rooms]
                # 确保提取的房间名称在标准房间名称列表中
                mentioned_rooms = [room for room in mentioned_rooms if room in room_names]
                self.logger.log(f"First Module:从用户指令中提取的房间信息:\n{mentioned_rooms}")
                return mentioned_rooms
            else:
                raise ValueError("Unknown response format from LLM.")
    
    def extract_rooms_from_home_info(self):
        """
        从家庭布局信息中提取房间名称。
        :return: 房间名称列表
        """
        try:
            # 解析 home_info 并提取房间名称
            room_names = [room["name"] for room in self.home_info["home"]["rooms"]]
            return room_names
        except Exception as e:
            self.logger.log(f"Error extracting room names from home info: {str(e)}", level="ERROR")
            return []
        
    def get_home_info(self, home_info_path):
        """
        读取home_info.json文件
        """
        try:
            # 获取当前文件的绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 构建配置文件的绝对路径
            abs_config_path = os.path.join(current_dir, home_info_path)
            
            with open(abs_config_path, "r", encoding='utf-8') as f:
                home_info = json.load(f)
            return home_info
        except FileNotFoundError:
                raise Exception(f"配置文件 {home_info_path} 未找到")
        except json.JSONDecodeError:
            raise Exception("配置文件格式错误")
        except Exception as e:
            raise Exception(f"报错: {str(e)}")
        
    def get_room_info_by_rooms(self, room_names):
        """
        根据房间名获取房间环境信息
        """
        try:
            environments = []
            for room_name in room_names:
                for room in self.home_info["home"]["rooms"]:
                    if room["name"] == room_name:
                        environments.append(room)
            return environments
        except Exception as e:
            self.logger.log(f"获取房间环境信息失败: {e}")
            return []
    
    def check_instruction_with_environment(self, instruction):
        """
        检查用户指令是否可以通过环境设备完成
        """
        # Step 1: 解析用户指令是否包含位置信息
        rooms = self.extract_rooms_from_instruction(instruction)
        # Step 2: 将用户自身位置也加入进去
        if rooms == []:
            rooms.append(self.location)
        # Step 3: 获取环境设备信息
        room_info = self.get_room_info_by_rooms(rooms)
        # Step 4: 将room_info转换为字符串
        room_info_dict = {room["name"]: room["devices"] for room in room_info}
        room_info_json = json.dumps(room_info_dict,ensure_ascii=False, indent=2)
        # self.logger.log(f"First Module:房间环境设备信息:\n{room_info_json}")
        # Step 4: 构建提示词
        prompt_template = PromptTemplate(
            input_variables=["instruction","room_info","user_location"],
            template=
            """
            You are a smart home AI assistant. Your task is to determine whether the user's instruction can be executed using the devices in the target room.
            Follow these rules:
            1. If the instruction explicitly mentions a room (e.g., "客厅", "卧室"), use that room as the target location.
            2. If the instruction does not mention a room, assume the user is referring to his current location: {user_location}.
            3. If the instruction can be executed using the devices in the target room, respond with the required devices in JSON format.
            4. If the instruction cannot be executed, respond with the reason in JSON format.

            User's current location: {user_location}

            Room information:
            {room_info}

            Instruction: {instruction}

            Response format:
            - If the instruction is executable:
                {{
                "status": "success",
                "instruction": "<user's original instruction>",
                "devices": [
                    {{
                    "type": "<device_type>",
                    "id": "<device_id>"
                    }},
                    ...
                ]
                }}
            - If the instruction is not executable:
                {{
                "status": "failed",
                "reason": "<reason>"
                }}

            Examples:
            - Instruction: "打开灯"
            User's current location: "guest_bedroom"
            Room information:
            {{
                "guest_bedroom": [
                    {{
                    "type": "light",
                    "id": "light_guest_bedroom",
                    "location": "center of ceiling",
                    "description": "control the brightness and color of lights in the second bedroom."
                    }}
                ]
            }}
            Response:
                {{
                "status": "success",
                "instruction": "打开灯",
                "devices": [
                    {{
                    "type": "light",
                    "id": "light_guest_bedroom"
                    }}
                ]
                }}

            - Instruction: "打开主卧的灯"
            User's current location: "living_room"
            Room information:
            {{
                "master_bedroom": [
                    {{
                    "type": "light",
                    "id": "light_master_bedroom",
                    "location": "bedside",
                    "description": "control the brightness and color of the lights in the master bedroom."
                    }}
                ]
            }}
            Response:
                {{
                "status": "success",
                "instruction": "打开主卧的灯",
                "devices": [
                    {{
                    "type": "light",
                    "id": "light_master_bedroom"
                    }}
                ]
                }}

            - Instruction: "打开厨房的空调"
            User's current location: "living_room"
            Room information:
            {{
                "kitchen": [
                    {{
                    "type": "light",
                    "id": "light_kitchen",
                    "location": "center of ceiling",
                    "description": "control the brightness and color of your kitchen lights."
                    }}
                ]
            }}
            Response:
                {{
                "status": "failed",
                "reason": "该指令不可执行，因为厨房没有空调。"
                }}
            """ 
        )
        # Step 5: 执行
        chain = prompt_template | self.llm
        response = chain.invoke({
            "instruction": instruction,
            "room_info": room_info_json,
            "user_location": self.location
        }).content
        self.logger.log(f"First Module:\n{response}")
        # Step 6: 解析输出
        if "```json" in response:
            result = response.split("```json")[1].split("```")[0].strip()
        else:
            result = response.strip()
        try:
            result_dict = json.loads(result)
            if result_dict["status"] == "success":
                return result
            elif result_dict["status"] == "failed":
                print(result_dict["reason"])
                return result
        except Exception as e:
            return json.dumps({"status": "error", "message": "Failed to parse the output."})

