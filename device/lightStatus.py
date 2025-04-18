from pydantic import BaseModel

# light 类型设备状态描述类
class LightStatus(BaseModel):
    device_id: str  # 设备id
    power: str  # 设备开关状态
    brightness: int  # 灯光亮度
    color: str  # 灯光颜色