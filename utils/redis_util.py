import redis
import json
import os

class RedisUtils:
    def __init__(self, config_path="../config/config.json"):
        """
        初始化 Redis 工具类
        :param config_path: 配置文件路径
        """
        try:
            # 获取当前文件的绝对路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 构建配置文件的绝对路径
            abs_config_path = os.path.join(current_dir, config_path)
            
            with open(abs_config_path, "r", encoding='utf-8') as f:
                config = json.load(f)

            redis_config = config.get("redis", {})
            host = redis_config.get("host", "localhost")
            port = redis_config.get("port", 6379)
            db = redis_config.get("db", 0)
            password = redis_config.get("password", None)

            self.redis_client = redis.StrictRedis(
                host=host,
                port=port,
                db=db,
                password=password,
                decode_responses=True
            )
        except FileNotFoundError:
            raise Exception(f"配置文件 {config_path} 未找到")
        except json.JSONDecodeError:
            raise Exception("配置文件格式错误")
        except Exception as e:
            raise Exception(f"无法连接到 Redis: {str(e)}")
        
    def set_value(self, key, value):
        """
        设置键值对。
        :param key: 键
        :param value: 值（可以是字符串、字典、列表等）
        """
        try:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)  # 将字典或列表转换为 JSON 字符串
            self.redis_client.set(key, value)
        except Exception as e:
            raise Exception(f"Redis 设置值失败: {str(e)}")

    def get_value(self, key):
        """
        获取键对应的值。
        :param key: 键
        :return: 值（如果是 JSON 字符串，会自动转换为字典或列表）
        """
        try:
            value = self.redis_client.get(key)
            if value is None:
                return None
            try:
                return json.loads(value)  # 尝试将值解析为 JSON
            except json.JSONDecodeError:
                return value  # 如果不是 JSON，直接返回原始值
        except Exception as e:
            raise Exception(f"Redis 获取值失败: {str(e)}")

    def delete_key(self, key):
        """
        删除键。
        :param key: 键
        """
        try:
            self.redis_client.delete(key)
        except Exception as e:
            raise Exception(f"Redis 删除键失败: {str(e)}")

    def key_exists(self, key):
        """
        检查键是否存在。
        :param key: 键
        :return: 布尔值，True 表示存在，False 表示不存在
        """
        try:
            return self.redis_client.exists(key)
        except Exception as e:
            raise Exception(f"Redis 检查键失败: {str(e)}")

