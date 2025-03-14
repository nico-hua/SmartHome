from utils.device_api import DeviceAPI
from utils.logger import Logger

class FilterModule:
    def __init__(self, retriever):
        self.retriever = retriever
        self.logger = Logger()
        self.device_api = DeviceAPI()

    def filter_devices(self, instruction):
        try:
            # Retrieve relevant devices based on instruction
            devices = self.device_api.get_devices_by_instruction(instruction)
            return devices
        except Exception as e:
            self.logger.log(f"Device Filtering Error: {str(e)}", level="ERROR")
            return []