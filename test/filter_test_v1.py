from v1.filter import FilterModule
import json

if __name__ == "__main__":

    # 家庭中已有的物理设备类型（英文）
    available_devices = ["air_conditioner", "light", "tv", "audio_player", "curtain"]

    # 初始化 Filter 模块
    filter_module = FilterModule(available_devices)

    # 测试: 明确指令
    instruction = "用户需要调亮客厅的灯光"
    result = filter_module.filter_devices(instruction)
    print(f"Filtered devices: {result}")