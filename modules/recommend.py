from utils.logger import Logger
from langchain_community.chat_models import ChatTongyi
import json

class RecommendModule:
    def __init__(self, home_info_path = "../config/home_info.json"):
        """
        初始化 RecommendModule 模块
        :param home_info_path: 家居环境信息路径
        """
        self.logger = Logger()
        self.home_info = self._get_home_info(home_info_path)
        self.llm = ChatTongyi(model="qwen-plus", temperature=0.1)

    def _get_home_info(self, home_info_path):
        """
        读取家居环境信息文件
        """
        try:
            with open(home_info_path, "r", encoding='utf-8') as f:
                home_info = json.load(f)
            return home_info
        except FileNotFoundError:
            raise Exception(f"配置文件 {home_info_path} 未找到")
        except json.JSONDecodeError:
            raise Exception("配置文件格式错误")
        except Exception as e:
            raise Exception(f"报错: {str(e)}")
        
    def _extract_location_from_instruction(self, instruction):
        """
        使用大模型从指令中提取房间信息
        """
        
