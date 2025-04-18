from utils.redis_util import RedisUtils

if __name__ == "__main__":
    redis_utils = RedisUtils()
    key = "Feedback:9d7e2911-ec8f-4f7f-91b9-7d8c994f05ef"
    result = redis_utils.get_value(key)
    print(result)