from pydantic import BaseModel

# Audioplayer 类型设备状态描述类
class AudioPlayerStatus(BaseModel):
    device_id: str  # 设备ID
    power: str  # 设备开关状态
    volume: int  # 音量大小
    music: str  # 播放的音乐名称