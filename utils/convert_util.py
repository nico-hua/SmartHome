from typing import List, Dict
from device.device_status import LightStatus, CurtainStatus, AirConditionerStatus, TelevisionStatus, AudioPlayerStatus, WindowStatus, HumidifierStatus, HeaterStatus, VentilationFanStatus, RangeHoodStatus, AirPurifierStatus

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

                elif device_info.device_type == "window":
                    device_entry["status"] = {"position": device_status.position}
                    device_entry["summary"] = f"窗户处于{'完全打开' if device_status.position == 100 else f'{device_status.position}% 打开'}状态。"

                elif device_info.device_type == "air_purifier":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "level": device_status.level
                    }
                    device_entry["summary"] = f"空气净化器已{'开启' if device_status.power == 'on' else '关闭'}，档位为{device_status.level}。"

                elif device_info.device_type == "humidifier":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "level": device_status.level
                    }
                    device_entry["summary"] = f"加湿器已{'开启' if device_status.power == 'on' else '关闭'}，档位为{device_status.level}。"

                elif device_info.device_type == "ventilation_fan":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "speed": device_status.speed
                    }
                    device_entry["summary"] = f"通风扇已{'开启' if device_status.power == 'on' else '关闭'}，风速档位为{device_status.speed}。"

                elif device_info.device_type == "range_hood":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "speed": device_status.speed
                    }
                    device_entry["summary"] = f"抽油烟机已{'开启' if device_status.power == 'on' else '关闭'}，风速档位为{device_status.speed}。"

                elif device_info.device_type == "heater":
                    device_entry["status"] = {
                        "power": device_status.power,
                        "level": device_status.level
                    }
                    device_entry["summary"] = f"暖气已{'开启' if device_status.power == 'on' else '关闭'}，档位为{device_status.level}。"

                else:
                    device_entry["summary"] = "未知设备类型，无法解析状态信息。"

                room_entry["devices"].append(device_entry)
            result["room_info"].append(room_entry)
    return result

def convert_device_info(device_full_info):
    """格式化单个设备的完整信息"""
    device_info = device_full_info.device_info
    device_status = device_full_info.device_status
    # 添加设备信息
    device_info_lines = [
        f"device_id: {device_info.device_id}",
        f"device_type: {device_info.device_type}",
        f"device_location: {device_info.location}",
        f"device_description: {device_info.description}"
    ]
    # 添加设备状态
    if device_status:
        if isinstance(device_status, LightStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, brightness is set to {device_status.brightness}, and color is {device_status.color}."
            )
        elif isinstance(device_status, AirConditionerStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, mode is set to {device_status.mode}, and temperature is {device_status.temperature}°C."
            )
        elif isinstance(device_status, AudioPlayerStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, currently playing '{device_status.music}', with volume at {device_status.volume}."
            )
        elif isinstance(device_status, CurtainStatus):
            device_info_lines.append(
                f"The current device status: its position is set to {device_status.position}."
            )
        elif isinstance(device_status, TelevisionStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, tuned to channel '{device_status.channel}', with volume at {device_status.volume}."
            )
        elif isinstance(device_status, WindowStatus):
            device_info_lines.append(
                f"The current device status: its position is set to {device_status.position}."
            )
        elif isinstance(device_status, AirPurifierStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, purification level is {device_status.level}."
            )
        elif isinstance(device_status, HumidifierStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, humidity level is {device_status.level}."
            )
        elif isinstance(device_status, VentilationFanStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, fan speed is {device_status.speed}."
            )
        elif isinstance(device_status, RangeHoodStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, fan speed is {device_status.speed}."
            )
        elif isinstance(device_status, HeaterStatus):
            device_info_lines.append(
                f"The current device status: power is {device_status.power}, heating level is {device_status.level}."
            )
    return "\n  - " + "\n  - ".join(device_info_lines)

def convert_environment_info(environment_info):
    """完整格式化环境信息"""
    descriptions = []
    for room_data in environment_info:
        for room_name, devices in room_data.items():
            device_infos = [convert_device_info(device) for device in devices]
            descriptions.append(f"{room_name}:" + "\n".join(device_infos))
    return "\n\n".join(descriptions)

def convert_recommended_devices_functions(recommended_devices_functions: List[Dict[str, List[str]]]) -> str:
    """ 将推荐设备的功能描述格式化为字符串，方便用于 prompt 插入 """
    formatted = []
    for device_func in recommended_devices_functions:
        for device, functions in device_func.items():
            func_lines = "\n  - " + "\n  - ".join(functions) if functions else "  - No available functions"
            formatted.append(f"{device}:\n{func_lines}")
    return "\n\n".join(formatted)