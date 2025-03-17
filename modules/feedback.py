from utils.logger import Logger
from utils.redis_util import RedisUtils

class FeedbackModule:
    def __init__(self, uuid):
        """
        初始化 FeedbackModule 模块
        :param uuid: 唯一标识符
        """
        self.logger = Logger()
        self.redis = RedisUtils()
        self.uuid = uuid

    def collect_feedback(self):
        """
        收集用户反馈
        """
        # Step 1: 询问用户是否满意
        while True:
            user_satisfaction = input("您对本次任务执行结果是否满意？(yes/no):").strip().lower()
            if user_satisfaction in ["yes", "no"]:
                break
            else:
                print("请输入yes或no！")        
        # Step 2: 将用户反馈存储到Redis中
        key = f"Feedback:{self.uuid}"
        if user_satisfaction == "yes":
            self.redis.set_value(key, {"status":"satisfied"})
        elif user_satisfaction == "no":
            user_feedback = input("请告诉我们需要注意的事项：").strip()
            self.redis.set_value(key, {"status":"unsatisfied", "feedback":user_feedback})
        return
        
