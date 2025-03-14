from modules.clarify import ClarifyModule
from modules.filter import FilterModule
from modules.plan import PlanModule
from modules.implement import ImplementModule
from modules.feedback import FeedbackModule
from rag.retriever import Retriever
from utils.logger import Logger

class SmartHomeAIAgent:
    def __init__(self):
        self.logger = Logger()
        self.retriever = Retriever()
        self.clarify_module = ClarifyModule(self.retriever)
        self.filter_module = FilterModule(self.retriever)
        self.plan_module = PlanModule(self.retriever)
        self.implement_module = ImplementModule()
        self.feedback_module = FeedbackModule(self.retriever)

    def process_instruction(self, user_input):
        try:
            # Step 1: Clarify the instruction
            clarified_instruction = self.clarify_module.clarify(user_input)
            self.logger.log(f"Clarified Instruction: {clarified_instruction}")

            # Step 2: Filter relevant devices
            devices = self.filter_module.filter_devices(clarified_instruction)
            self.logger.log(f"Filtered Devices: {devices}")

            # Step 3: Generate task plan
            task_plan = self.plan_module.generate_plan(clarified_instruction, devices)
            self.logger.log(f"Generated Task Plan: {task_plan}")

            # Step 4: Execute the plan
            execution_result = self.implement_module.execute(task_plan)
            self.logger.log(f"Execution Result: {execution_result}")

            # Step 5: Collect feedback
            feedback = self.feedback_module.collect_feedback(user_input, execution_result)
            self.logger.log(f"User Feedback: {feedback}")

            return execution_result
        except Exception as e:
            self.logger.log(f"Error: {str(e)}", level="ERROR")
            return None

if __name__ == "__main__":
    agent = SmartHomeAIAgent()
    user_input = "我太冷了"
    result = agent.process_instruction(user_input)
    print(result)