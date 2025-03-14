from modules.implement import ImplementModule

if __name__ == "__main__":
    # 初始化 Implement 模块
    implement_module = ImplementModule()

    # 测试: 明确任务计划
    task_plan = [
        "1. Turn off the lights.",
        "2. Turn on the TV.",
        "3. Set the air conditioner temperature to 26°C."
        "4. Set the speaker volume to 50%."
    ]
    device_apis = {
        "light": "light.set_brightness(brightness: int)",
        "tv": "tv.set_power(status: bool)",
        "speaker": "speaker.set_volume(volume: int)",
        "air_conditioner": "air_conditioner.set_temperature(temperature: int)"
    }
    result = implement_module.generate_code(task_plan, device_apis)
    print(f"Generated Python Code:\n{result}")