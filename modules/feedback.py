from utils.logger import Logger
import redis
import json


class FeedbackModule:
    def __init__(self, redis_host="localhost", redis_port=6379, redis_db=0):
        """
        初始化 Feedback 模块。
        :param redis_host: Redis 主机地址
        :param redis_port: Redis 端口
        :param redis_db: Redis 数据库编号
        """
        self.logger = Logger()
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

    def feedback():
        pass