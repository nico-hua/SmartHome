from utils.redis_util import RedisUtils

if __name__ == "__main__":
    redis_utils = RedisUtils()
    key = "test_key"
    value = "test_value"
    redis_utils.set_value(key, value)
    result = redis_utils.get_value(key)
    print(result)