from modules.implement import ImplementModule

if __name__ == "__main__":
    # 初始化 Implement 模块
    implement_module = ImplementModule()

    # 测试1: 明确任务计划
    task_plan = [
        "1. 调暗客厅的灯光至 20% 亮度。",
        "2. 关闭窗帘。",
        "3. 打开空调并设置为 24°C 的制冷模式。",
        "4. 打开电视并切换到 HDMI 1 频道。",
        "5. 打开音响并设置音量为 70%。",
        "6. 播放音乐《白日忽一梦》。"
    ]

    # 设备的api描述
    device_apis = {
        "light": """
        - light.set_brightness(brightness: int): Set the light brightness, the brightness value is 0-100.
        - light.set_color(color: str): Set the light color. The color value is a string (such as "red", "blue").
        - light.turn_on(): Turn on the lights.
        - light.turn_off(): Turn off the lights.
        """,
        "tv": """
        - tv.set_power(status: bool): Set the TV power state, True for on, False for off.
        - tv.set_channel(channel: int): Set the TV channel. The channel number is an integer.
        - tv.set_volume(volume: int): Set the TV volume, the volume value is 0-100.
        """,
        "speaker": """
        - speaker.set_volume(volume: int): Set the audio volume, the volume value is 0-100.
        - speaker.play_music(song: str): Play music, song is the song title.
        - speaker.stop_music(): Stop playing music.
        """,
        "air_conditioner": """
        - air_conditioner.set_temperature(temperature: int): Set the air conditioning temperature. The temperature value is an integer.
        - air_conditioner.set_mode(mode: str): Set the air conditioning mode. The mode value is a string (such as "cool", "heat").
        - air_conditioner.turn_on(): Turn on the air conditioner.
        - air_conditioner.turn_off(): Turn off the air conditioner.
        """,
        "curtain": """
        - curtain.open(): Open the curtains.
        - curtain.close(): Close the curtains.
        - curtain.set_position(position: int): Set the curtain position, the position value is 0-100 (0: fully closed, 100: fully open).
        """
    }

    # 生成 Python 代码
    generated_code = implement_module.generate_code(task_plan, device_apis)
    print(f"Generated Python Code:\n{generated_code}")

    # 执行生成的代码
    implement_module.execute_code(generated_code)