from utils.chroma_util import ChromaUtils
from device.device_api_info import device_api_store
import json

chroma = ChromaUtils()
# chroma.init_chroma_collection()
# for api in device_api_store:
#     chroma.embed_and_store_instruction(
#         id=api["id"],
#         description=api["description"],
#         api=api["api"],
#         args_num=api["args_num"]
#     )
result = chroma.retrieve_similar_instructions("Set the TV volume.", top_k=1)
api = json.loads(result)
print(api["id"])
print(api["description"])
print(api["api"])
print(api["args_num"])