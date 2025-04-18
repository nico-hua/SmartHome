from pydantic import BaseModel

# 设备描述类
class DeviceInfo(BaseModel):
    device_id: str  # 设备ID
    device_type: str  # 设备类型
    location: str  # 设备位置
    description: str  # 设备描述
    room: str  # 设备所在房间