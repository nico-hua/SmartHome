from pydantic import BaseModel

# light 类型设备状态描述类
class LightStatus(BaseModel):
    device_id: str  # 设备id
    power: str  # 设备开关状态
    brightness: int  # 灯光亮度
    color: str  # 灯光颜色

# Television 类型设备状态描述类
class TelevisionStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 电源状态
    channel: str  # 当前频道
    volume: int  # 音量

# Audioplayer 类型设备状态描述类
class AudioPlayerStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 设备开关状态
    volume: int  # 音量大小
    music: str  # 播放的音乐名称

# AirConditioner 类型设备状态描述类
class AirConditionerStatus(BaseModel):
    device_id:str  # 设备ID
    power:str  # 开关状态
    mode:str  # 模式
    temperature:int  # 温度

# Curtain 类型设备状态描述类
class CurtainStatus(BaseModel):
    device_id: str  # 设备ID
    position: int  # 百分比，0-100

#  Window 类型设备状态描述类
class WindowStatus(BaseModel):
    device_id: str  # 设备ID
    position: int  # 百分比，0-100

# AirPurifier 类型设备状态描述类
class AirPurifierStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 开关状态
    level: str  # 档位

# Humidifier 类型设备状态描述类
class HumidifierStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 开关状态
    level: int  # 档位

# VentilationFan 类型设备状态描述类
class VentilationFanStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 开关状态
    speed: str  # 风速

# RangeHood 类型设备状态描述类
class RangeHoodStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 开关状态
    speed: str  # 风速

# Heater 类型设备状态描述类
class HeaterStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 开关状态
    level: str  # 档位