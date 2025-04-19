from collections import defaultdict
import pymysql
import os
import json
from typing import List, Dict
from device.deviceFullInfo import DeviceFullInfo
from device.deviceInfo import DeviceInfo
from device.lightStatus import LightStatus
from device.curtainStatus import CurtainStatus
from device.airconditionerStatus import AirConditionerStatus
from device.televisionStatus import TelevisionStatus
from device.audioplayerStatus import AudioPlayerStatus

class MySQLUtils:
    def __init__(self, config_path="../config/config.json"):
        """
        初始化 MySQL 工具类
        :param config_path: 配置文件路径
        """
        try:
            # 获取当前文件的绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 构建配置文件的绝对路径
            abs_config_path = os.path.join(current_dir, config_path)
            
            with open(abs_config_path, "r", encoding='utf-8') as f:
                config = json.load(f)

            mysql_config = config.get("mysql", {})
            host = mysql_config.get("host", "localhost")
            port = mysql_config.get("port", 3306)
            user = mysql_config.get("user", "root")
            db = mysql_config.get("database", "smart_home")
            password = mysql_config.get("password", "123456a")

            self.client = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except FileNotFoundError:
            raise Exception(f"配置文件 {config_path} 未找到")
        except json.JSONDecodeError:
            raise Exception("配置文件格式错误")
        except Exception as e:
            raise Exception(f"无法连接到 Mysql: {str(e)}")
        
    def get_device_full_info_by_room(self, room: str) -> List[DeviceFullInfo]:

        """
        根据房间名称获取设备的完整信息
        :param room: 房间名称
        :return: 设备完整信息列表
        """
        with self.client.cursor() as cursor:
            # 获取房间内全部设备信息
            cursor.execute("SELECT * FROM room_info WHERE room = %s", (room,))
            device_infos = [DeviceInfo(**item) for item in cursor.fetchall()]
            # 如果为空，则返回空列表
            if not device_infos:
                return []
            # 按设备类型分组
            device_groups = defaultdict(list)
            for device_info in device_infos:
                device_groups[device_info.device_type].append(device_info.device_id)
            # 获取设备状态
            status_map = {}
            for device_type, device_ids in device_groups.items():
                if device_type == 'light':
                    cursor.execute(f"SELECT * FROM light WHERE device_id IN ({','.join(['%s']*len(device_ids))})", device_ids)
                    for item in cursor.fetchall():
                        status_map[item['device_id']] = LightStatus(**item)
                elif device_type == 'air_conditioner':
                    cursor.execute(f"SELECT * FROM air_conditioner WHERE device_id IN ({','.join(['%s']*len(device_ids))})", device_ids)
                    for item in cursor.fetchall():
                        status_map[item['device_id']] = AirConditionerStatus(**item)
                elif device_type == 'television':
                        cursor.execute(f"SELECT * FROM television WHERE device_id IN ({','.join(['%s']*len(device_ids))})", device_ids)
                        for item in cursor.fetchall():
                            status_map[item['device_id']] = TelevisionStatus(**item)
                elif device_type == 'audio_player':
                        cursor.execute(f"SELECT * FROM audio_player WHERE device_id IN ({','.join(['%s']*len(device_ids))})", device_ids)
                        for item in cursor.fetchall():
                            status_map[item['device_id']] = AudioPlayerStatus(**item)
                elif device_type == 'curtain':
                        cursor.execute(f"SELECT * FROM curtain WHERE device_id IN ({','.join(['%s']*len(device_ids))})", device_ids)
                        for item in cursor.fetchall():
                            status_map[item['device_id']] = CurtainStatus(**item)
            # 组合结果
            result = []
            for device_info in device_infos:
                result.append(DeviceFullInfo(
                    device_info=device_info,
                    device_status=status_map.get(device_info.device_id, None)
                ))
            return result
        
    def get_device_function_by_type(self, device_type: str) -> List[str]:
        """
        根据设备类型获取设备功能
        :param device_type: 设备类型
        :return: 设备功能列表
        """
        with self.client.cursor() as cursor:
            cursor.execute("SELECT function_description FROM device_function WHERE device_type_name = %s", (device_type,))
            results = cursor.fetchall()
            return [result['function_description'] for result in results]
        
    def get_recommended_devices_functions(self, recommended_devices: List[str]) -> List[Dict[str, List[str]]]:
        """ 获取推荐设备的功能描述 """
        devices_functions = []
        for device in recommended_devices:
            device_functions = self.get_device_function_by_type(device)
            devices_functions.append({device:device_functions})
        # 关闭数据库连接
        self.close()
        return devices_functions

            
    def close(self):
        """ 关闭数据库连接 """
        self.client.close()

            