from utils.mysql_util import MySQLUtils
from device.deviceFullInfo import DeviceFullInfo
from device.deviceInfo import DeviceInfo
from device.lightStatus import LightStatus
from device.curtainStatus import CurtainStatus
from device.airconditionerStatus import AirConditionerStatus
from device.televisionStatus import TelevisionStatus
from device.audioplayerStatus import AudioPlayerStatus
from utils.convert_util import convert_room_info_to_json
import json
from state.globalState import GlobalState, ClarifyResponse

def structured_response(content: str):
        """处理结构化输出，兼容多种格式：
        1. 标准 tool_calls 格式
        2. ```json 标记格式
        3. ✦FUNCTION✿: 前缀格式
        """
        response = None

        # ```json 标记格式
        if "```json" in content:
            try:
                response = ClarifyResponse(json.loads(content.split("```json")[1].split("```")[0].strip()))
            except Exception as e:
                response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

        # ✦FUNCTION✿: 前缀格式
        if "require_device" in content and "instruction_response" in content:
            # 尝试从非标准内容中提取 JSON
            args_start = content.find("{")
            args_end = content.rfind("}") + 1
            args_json = content[args_start:args_end]
            print(args_json)
            try:
                response = ClarifyResponse(**json.loads(args_json))
            except Exception as e:
                response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

        return response

if __name__ == "__main__":
    content = "✦FUNCTION✿: ClarifyResponse\n✦ARGS✿: {\"require_device\": true, \"instruction_response\": \"\"}"
    print(structured_response(content))


