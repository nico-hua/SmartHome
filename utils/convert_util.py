from typing import List, Dict

def convert_room_info_to_json(room_info: List[Dict]):
    """
    将房间信息转换为json格式
    :param room_info: 房间信息列表
    :return: json格式的房间信息
    """
    result = {"room_info": []}
    for room_dict in room_info:
        for room, devices in room_dict.items():
            room_entry = {"room": room, "devices": []}
            for device in devices:
                device_info = device.device_info
                device_status = device.device_status
                device_entry = {
                    "device_id": device_info.device_id,
                    "device_type": device_info.device_type,
                    "location": device_info.location,
                    "description": device_info.description,
                    "status": {},
                    "summary": ""
                }

                # 填充状态字段和摘要
                if device_info.device_type == "air_conditioner":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "mode": device_status.mode,
                        "temperature": device_status.temperature
                    }
                    device_entry["summary"] = f"空调已{'开启' if device_status.power == 'on' else '关闭'}，模式为{device_status.mode}，温度设定为{device_status.temperature}度。"

                elif device_info.device_type == "curtain":
                    device_entry["status"] = {"position": device_status.position}
                    device_entry["summary"] = f"窗帘处于{'完全打开' if device_status.position == 100 else f'{device_status.position}% 打开'}状态。"

                elif device_info.device_type == "light":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "brightness": device_status.brightness,
                        "color": device_status.color
                    }
                    device_entry["summary"] = f"灯光已{'开启' if device_status.power == 'on' else '关闭'}，亮度{device_status.brightness}%，颜色为{device_status.color}。"

                elif device_info.device_type == "audio_player":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "volume": device_status.volume,
                        "music": device_status.music
                    }
                    device_entry["summary"] = f"音响已{'开启' if device_status.power == 'on' else '关闭'}，音量{device_status.volume}，正在播放《{device_status.music}》。"

                elif device_info.device_type == "television":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "volume": device_status.volume,
                        "channel": device_status.channel
                    }
                    device_entry["summary"] = f"电视已{'开启' if device_status.power == 'on' else '关闭'}，频道为{device_status.channel}，音量为{device_status.volume}。"

                else:
                    device_entry["summary"] = "未知设备类型，无法解析状态信息。"

                room_entry["devices"].append(device_entry)
            result["room_info"].append(room_entry)
    return result
