from pydantic import BaseModel

# Television 类型设备状态描述类
class TelevisionStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 电源状态
    channel: str  # 当前频道
    volume: int  # 音量