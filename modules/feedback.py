from utils.logger import Logger

class FeedbackModule:
    def __init__(self, retriever):
        self.retriever = retriever
        self.logger = Logger()

    def collect_feedback(self, user_input, execution_result):
        try:
            # Collect feedback from the user
            feedback = input("Was the execution satisfactory? (yes/no): ")
            if feedback.lower() == "no":
                detailed_feedback = input("Please provide detailed feedback: ")
                self.retriever.store_feedback(user_input, detailed_feedback)
            return feedback
        except Exception as e:
            self.logger.log(f"Feedback Collection Error: {str(e)}", level="ERROR")
            return None