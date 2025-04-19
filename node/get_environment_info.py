from state.globalState import GlobalState
from utils.mysql_util import MySQLUtils

def get_environment_info(state: GlobalState):
    """" 获取环境信息 """
    target_location = state['target_location']
    mysql = MySQLUtils()
    environment_info = []
    # 分别获取每个房间的环境信息
    for room in target_location:
        room_data = {room: mysql.get_device_full_info_by_room(room)}
        environment_info.append(room_data)
    # 关闭数据库连接
    mysql.close()
    return {**state, 'environment_info': environment_info}