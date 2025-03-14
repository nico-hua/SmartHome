from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from utils.logger import Logger

class PlanModule:
    def __init__(self, retriever):
        self.retriever = retriever
        self.logger = Logger()
        self.llm = OpenAI(temperature=0.7)
        self.prompt = PromptTemplate(
            input_variables=["instruction", "devices"],
            template="Generate a task plan for the following instruction: {instruction} using devices: {devices}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_plan(self, instruction, devices):
        try:
            task_plan = self.chain.run({"instruction": instruction, "devices": devices})
            return task_plan
        except Exception as e:
            self.logger.log(f"Task Planning Error: {str(e)}", level="ERROR")
            return []