from pydantic import BaseModel
from device.deviceInfo import DeviceInfo
from typing import Optional

# 设备信息和设备状态
class DeviceFullInfo(BaseModel):
    device_info: DeviceInfo
    device_status: Optional[BaseModel]  # 可以是LightStatus、AirConditionerStatus等