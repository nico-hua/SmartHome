from modules.plan import PlanModule

if __name__ == "__main__":
    planModule = PlanModule()
    planModule.generate_plan("test", "用户需要调整灯光、音乐和温度等设备来准备派对。", ["light", "tv", "audio_player", "air_conditioner"])