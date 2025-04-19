from pydantic import BaseModel
from device.device_info import DeviceInfo
from typing import Optional

# 设备信息和设备状态
class DeviceFullInfo(BaseModel):
    device_info: DeviceInfo
    device_status: Optional[BaseModel]  # 可以是LightStatus、AirConditionerStatus等