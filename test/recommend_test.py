from v2.recommend import RecommendModule

if __name__ == "__main__":
    home_info_path = "../config/home_info.json"
    recommendModule = RecommendModule("uuid", home_info_path, "master_bedroom")
    recommendModule.check_instruction_with_environment("打开主卧和次卧的灯")
    