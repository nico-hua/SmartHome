from modules.first import FirstModule

if __name__ == "__main__":
    home_info_path = "../config/home_info.json"
    firstModule = FirstModule("uuid", home_info_path, "living_room")
    firstModule.check_instruction_with_environment("打开主卧的空调")
    