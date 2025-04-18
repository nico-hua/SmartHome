from langchain_core.tools import tool
from pydantic import field_validator, ValidationError, BaseModel, Field
from typing import List
from utils.mysql_util import MySQLUtils
from utils.convert_util import convert_room_info_to_json

# 默认房间列表
DEFAULT_ROOM_NAMES = ["living_room", "master_bedroom", "guest_bedroom", "kitchen", "bathroom"]

# 定义输入的 Schema
class GetRoomInfoSchema(BaseModel):
    rooms: List[str] = Field(description="Room name list, can only be the five predefined ones")

    @field_validator("rooms")
    @classmethod
    def validate_rooms(cls, rooms):
        for room in rooms:
            if room not in DEFAULT_ROOM_NAMES:
                raise ValidationError(f"Invalid room name: {room}. Valid options are: {DEFAULT_ROOM_NAMES}")
        return rooms

@tool(args_schema=GetRoomInfoSchema)
def get_room_info(rooms: List[str]):
    """
    查询房间内的设备信息。
    输入: {'rooms': ['living_room', 'kitchen']}
    返回: {'room_info': [
            {'room': 'living_room', 'devices': [设备信息...]},
            {'room': 'kitchen', 'devices': [设备信息...]}
        ]}
    """
    room_info = []

    # 数据库配置
    mysql = MySQLUtils()

    # 获取各房间的设备信息
    for room in rooms:
        room_data = {room: mysql.get_device_full_info_by_room(room)}
        room_info.append(room_data)

    return convert_room_info_to_json(room_info)