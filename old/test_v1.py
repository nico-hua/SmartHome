from v1.clarify import ClarifyModule
from v1.filter import FilterModule
from v1.plan import PlanModule
from v1.implement import ImplementModule
from v1.feedback import FeedbackModule
from tools.rag import RAGModule
import json
import uuid

if __name__ == "__main__":
    # 使用UUID区分每次流程
    uuid = str(uuid.uuid4())
    print("UUID:", uuid)
    user_input = input("请输入指令：")
    # 澄清模块
    clarify_module = ClarifyModule(uuid)
    clarify_result = clarify_module.interact_with_user(user_input)
    clarify_result_dict = json.loads(clarify_result)
    if clarify_result_dict["status"] == "success" :
        instruction = clarify_result_dict["instruction"]
        # 过滤模块
        available_devices = ["air_conditioner", "light", "tv", "audio_player", "curtain"]
        filter_module = FilterModule(available_devices, uuid, instruction)
        filter_result = filter_module.filter_devices()
        filter_result_dict = json.loads(filter_result)
        if filter_result_dict["status"] == "success" :
            filtered_devices = filter_result_dict["devices"]
            # 计划模块
            device_descriptions = {
                "light": "Turns the light on/off, gets the current birghtness, and controls brightness and color, and .",
                "air_conditioner": "Controls the temperature and mode of the air conditioner, and get the current air conditioning temperature.",
                "tv": "Controls power, channel, and volume of the TV.",
                "audio_player": "Controls volume, plays and stops music.",
                "curtain": "Controls the position of the curtain, opens and closes it."
            }
            filtered_device_descriptions = {device: device_descriptions[device] for device in filtered_devices}
            plan_module = PlanModule(uuid,instruction, filtered_device_descriptions)
            plan_result = plan_module.generate_plan()
            # 执行模块
            device_apis = {
                "light": """
                - light.turn_on(): Turn on the lights.
                - light.turn_off(): Turn off the lights.
                - light.get_brightness(): Return the current light brightness, the brightness value is 0-100..
                - light.set_brightness(brightness: int): Set the light brightness, the brightness value is 0-100.
                - light.set_color(color: str): Set the light color. The color value is a string (such as "red", "blue").
                """,
                "tv": """
                - tv.set_power(status: bool): Set the TV power state, True for on, False for off.
                - tv.set_channel(channel: int): Set the TV channel. The channel number is an integer.
                - tv.set_volume(volume: int): Set the TV volume, the volume value is 0-100.
                """,
                "audio_player": """
                - audio_player.set_volume(volume: int): Set the audio volume, the volume value is 0-100.
                - audio_player.play_music(song: str): Play music, song is the song title.
                - audio_player.stop_music(): Stop playing music.
                """,
                "air_conditioner": """
                - air_conditioner.turn_on(): Turn on the air conditioner.
                - air_conditioner.turn_off(): Turn off the air conditioner.
                - air_conditioner.set_temperature(temperature: int): Set the air conditioning temperature. The temperature value is an integer.
                - air_conditioner.set_mode(mode: str): Set the air conditioning mode. The mode value is a string (such as "cool", "heat").
                - air_conditioner.get_temperature(): Return the current air conditioning temperature.
                """,
                "curtain": """
                - curtain.open(): Open the curtains.
                - curtain.close(): Close the curtains.
                - curtain.set_position(position: int): Set the curtain position, the position value is 0-100 (0: fully closed, 100: fully open).
                """
            }
            filtered_device_apis = {device: device_apis[device] for device in filtered_devices}
            implement_module = ImplementModule(uuid)
            implement_result = implement_module.generate_code(plan_result, filtered_device_apis)
            implement_result = implement_module.execute_code(implement_result)
            if implement_result == "SUCCESS":
                # 将澄清指令存储到向量数据库
                rag = RAGModule()
                rag.embed_and_store_instruction(instruction, uuid)
                # 反馈模块
                feedback_module = FeedbackModule(uuid)
                feedback_module.collect_feedback()
            else:
                print(implement_result)
        else:
            print(filter_result_dict["reason"])
    else:
        print(clarify_result_dict["reason"])