from modules.filter import FilterModule
import json

if __name__ == "__main__":

    # 家庭中已有的物理设备类型（英文）
    available_devices = ["air_conditioner", "light", "tv", "speaker", "curtain"]

    # 初始化 Filter 模块
    filter_module = FilterModule(available_devices)

    # 测试: 明确指令
    instruction = "用户需要调整灯光音乐来开派对"
    result = filter_module.filter_devices(instruction)
    print(f"Filtered devices: {result}")

    # 获取设备类型
    result_dict = json.loads(result)
    devices = result_dict["devices"]
    for device in devices:
        print(device)