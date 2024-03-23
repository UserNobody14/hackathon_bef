# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.llms.octoai_endpoint import OctoAIEndpoint
# from dotenv import load_dotenv
# import os
# from langchain_community.embeddings import OctoAIEmbeddings
# from langchain_community.vectorstores import Milvus

# template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.\n Instruction:\n{question}\n Response: """
# prompt = PromptTemplate.from_template(template)

# load_dotenv()
# os.environ["OCTOAI_API_TOKEN"] = (
#     "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiJiMjA2Zjk4OS01N2JjLTQ2ZGItYmVkYi05MTNiMGIxODMzYzgiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiI4ZjM3NzEwMi03ZDM0LTQ5MTktOTQ2Ni04OTYxMTM5MzFkOWEiLCJ1c2VySWQiOiJiYjBmZGU0My1hY2NkLTQ5ZjMtYmM0YS0yYTBiNzNlM2M5ZTAiLCJyb2xlcyI6WyJGRVRDSC1ST0xFUy1CWS1BUEkiXSwicGVybWlzc2lvbnMiOlsiRkVUQ0gtUEVSTUlTU0lPTlMtQlktQVBJIl0sImF1ZCI6IjNkMjMzOTQ5LWEyZmItNGFiMC1iN2VjLTQ2ZjYyNTVjNTEwZSIsImlzcyI6Imh0dHBzOi8vaWRlbnRpdHkub2N0b21sLmFpIiwiaWF0IjoxNzExMjExODAxfQ.GaaXvPGgp40CT5r-PTzaOoIHm28VTkx49utRAar6xIbu2vaduQya3IoodjxuwkWpLmwRDZzxO6yzmkD69KvN9_R0PcIwPSmg01DARubTmvbzPFMPzynbvdJrN27sNrjaxdJBYahL9vkI4Jr7lbuihy79-TpOHtQVwta0HfsNcHZPHD-P6pm4gPjN6U_9TpbaPJFDBeOFHzCXsX8-yhihT6apfo8PKZMZiNi257WrC8TTBqYA6yLeRP8hmtEv1GVHTT9tVtmqMYT5f2JiRlWYPawc2ehDZS3BMDNoFr3pKpLcN5h6OScf-NZI7oTRgWUu968RqpZKsILyPcu9BCCq1A"
# )

# llm = OctoAIEndpoint(
#     endpoint_url="https://text.octoai.run/v1/chat/completions",
#     octoai_api_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiJiMjA2Zjk4OS01N2JjLTQ2ZGItYmVkYi05MTNiMGIxODMzYzgiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiI4ZjM3NzEwMi03ZDM0LTQ5MTktOTQ2Ni04OTYxMTM5MzFkOWEiLCJ1c2VySWQiOiJiYjBmZGU0My1hY2NkLTQ5ZjMtYmM0YS0yYTBiNzNlM2M5ZTAiLCJyb2xlcyI6WyJGRVRDSC1ST0xFUy1CWS1BUEkiXSwicGVybWlzc2lvbnMiOlsiRkVUQ0gtUEVSTUlTU0lPTlMtQlktQVBJIl0sImF1ZCI6IjNkMjMzOTQ5LWEyZmItNGFiMC1iN2VjLTQ2ZjYyNTVjNTEwZSIsImlzcyI6Imh0dHBzOi8vaWRlbnRpdHkub2N0b21sLmFpIiwiaWF0IjoxNzExMjExODAxfQ.GaaXvPGgp40CT5r-PTzaOoIHm28VTkx49utRAar6xIbu2vaduQya3IoodjxuwkWpLmwRDZzxO6yzmkD69KvN9_R0PcIwPSmg01DARubTmvbzPFMPzynbvdJrN27sNrjaxdJBYahL9vkI4Jr7lbuihy79-TpOHtQVwta0HfsNcHZPHD-P6pm4gPjN6U_9TpbaPJFDBeOFHzCXsX8-yhihT6apfo8PKZMZiNi257WrC8TTBqYA6yLeRP8hmtEv1GVHTT9tVtmqMYT5f2JiRlWYPawc2ehDZS3BMDNoFr3pKpLcN5h6OScf-NZI7oTRgWUu968RqpZKsILyPcu9BCCq1A",
#     model_kwargs={
#         "model": "mixtral-8x7b-instruct-fp16",
#         "max_tokens": 128,
#         "presence_penalty": 0,
#         "temperature": 0.01,
#         "top_p": 0.9,
#         "messages": [
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant. Keep your responses limited to one short paragraph if possible.",
#             },
#         ],
#     },
# )


# def ask_question(question: str, prompt: PromptTemplate = prompt):
#     llm_chain = LLMChain(prompt=prompt, llm=llm)
#     return llm_chain.invoke(question)["text"]
