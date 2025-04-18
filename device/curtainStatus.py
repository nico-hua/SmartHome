from pydantic import BaseModel

# Curtain 类型设备状态描述类
class CurtainStatus(BaseModel):
    device_id: str  # 设备ID
    position: int  # 百分比，0-100