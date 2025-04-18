from v1.clarify import ClarifyModule

if __name__ == "__main__":
    clarify_module = ClarifyModule()

    user_input = "我准备开一个party"
    result = clarify_module.interact_with_user(user_input)
    print(f"澄清后的指令: {result}")