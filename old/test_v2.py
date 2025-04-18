from v2.recommend import RecommendModule
from v2.plan import PlanModule
from v2.implement import ImplementModule
from tools.rag import RAGModule
import json
import uuid

if __name__ == "__main__":
    # 使用UUID区分每次流程
    uuid = str(uuid.uuid4())
    print("UUID:", uuid)
    instruction = input("请输入指令：")
    # 假定可以通过某种手段获知用户在哪个房间
    location = "master_bedroom"
    # 推荐模块
    recommendModule = RecommendModule()
    recommend_result = recommendModule.check_instruction_with_environment(uuid, instruction, location)
    recommend_result_dict = json.loads(recommend_result)
    if recommend_result_dict["status"] == "success":
        instruction = recommend_result_dict["instruction"]
        recommend_devices = recommend_result_dict["devices"]
        # 计划模块
        planModule = PlanModule()
        plan_result = planModule.generate_plan(uuid, instruction, recommend_devices, location)
        # 执行模块
        implementModule = ImplementModule()
        implement_code = implementModule.generate_code(uuid, plan_result, recommend_devices)
        implementModule.execute_code(implement_code)
    else:
        print(recommend_result_dict["reason"])
