from pydantic import BaseModel

# AirConditioner 类型设备状态描述类
class AirConditionerStatus(BaseModel):
    device_id:str  # 设备ID
    power:str  # 开关状态
    mode:str  # 模式
    temperature:int  # 温度