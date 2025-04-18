from v1.plan import PlanModule

if __name__ == "__main__":
    # 初始化 Plan 模块
    plan_module = PlanModule()

    # 测试1: 明确指令
    instruction = "用户需要调整灯光、音乐和温度等设备来准备派对。"
    device_descriptions = {
        "light": "controls the brightness of lights",
        "tv": "turns the TV on/off",
        "audio_player": "controls audio output",
        "air_conditioner": "controls the temperature of the room"
    }
    result = plan_module.generate_plan(instruction, device_descriptions)
    print(f"Generated Plan: {result}")