from langchain_community.embeddings import OctoAIEmbeddings

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint
from langchain_community.vectorstores import Milvus
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_core.runnables import RunnablePassthrough

# from dotenv import load_dotenv
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

# import os


# load_dotenv()
# os.environ["OCTOAI_API_TOKEN"] = (
#     "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiJiMjA2Zjk4OS01N2JjLTQ2ZGItYmVkYi05MTNiMGIxODMzYzgiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiI4ZjM3NzEwMi03ZDM0LTQ5MTktOTQ2Ni04OTYxMTM5MzFkOWEiLCJ1c2VySWQiOiJiYjBmZGU0My1hY2NkLTQ5ZjMtYmM0YS0yYTBiNzNlM2M5ZTAiLCJyb2xlcyI6WyJGRVRDSC1ST0xFUy1CWS1BUEkiXSwicGVybWlzc2lvbnMiOlsiRkVUQ0gtUEVSTUlTU0lPTlMtQlktQVBJIl0sImF1ZCI6IjNkMjMzOTQ5LWEyZmItNGFiMC1iN2VjLTQ2ZjYyNTVjNTEwZSIsImlzcyI6Imh0dHBzOi8vaWRlbnRpdHkub2N0b21sLmFpIiwiaWF0IjoxNzExMjExODAxfQ.GaaXvPGgp40CT5r-PTzaOoIHm28VTkx49utRAar6xIbu2vaduQya3IoodjxuwkWpLmwRDZzxO6yzmkD69KvN9_R0PcIwPSmg01DARubTmvbzPFMPzynbvdJrN27sNrjaxdJBYahL9vkI4Jr7lbuihy79-TpOHtQVwta0HfsNcHZPHD-P6pm4gPjN6U_9TpbaPJFDBeOFHzCXsX8-yhihT6apfo8PKZMZiNi257WrC8TTBqYA6yLeRP8hmtEv1GVHTT9tVtmqMYT5f2JiRlWYPawc2ehDZS3BMDNoFr3pKpLcN5h6OScf-NZI7oTRgWUu968RqpZKsILyPcu9BCCq1A"
# )
# embeddings = OctoAIEmbeddings(endpoint_url="https://text.octoai.run/v1/embeddings")

llm = OctoAIEndpoint(
    endpoint_url="https://text.octoai.run/v1/chat/completions",
    octoai_api_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiJiMjA2Zjk4OS01N2JjLTQ2ZGItYmVkYi05MTNiMGIxODMzYzgiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiI4ZjM3NzEwMi03ZDM0LTQ5MTktOTQ2Ni04OTYxMTM5MzFkOWEiLCJ1c2VySWQiOiJiYjBmZGU0My1hY2NkLTQ5ZjMtYmM0YS0yYTBiNzNlM2M5ZTAiLCJyb2xlcyI6WyJGRVRDSC1ST0xFUy1CWS1BUEkiXSwicGVybWlzc2lvbnMiOlsiRkVUQ0gtUEVSTUlTU0lPTlMtQlktQVBJIl0sImF1ZCI6IjNkMjMzOTQ5LWEyZmItNGFiMC1iN2VjLTQ2ZjYyNTVjNTEwZSIsImlzcyI6Imh0dHBzOi8vaWRlbnRpdHkub2N0b21sLmFpIiwiaWF0IjoxNzExMjExODAxfQ.GaaXvPGgp40CT5r-PTzaOoIHm28VTkx49utRAar6xIbu2vaduQya3IoodjxuwkWpLmwRDZzxO6yzmkD69KvN9_R0PcIwPSmg01DARubTmvbzPFMPzynbvdJrN27sNrjaxdJBYahL9vkI4Jr7lbuihy79-TpOHtQVwta0HfsNcHZPHD-P6pm4gPjN6U_9TpbaPJFDBeOFHzCXsX8-yhihT6apfo8PKZMZiNi257WrC8TTBqYA6yLeRP8hmtEv1GVHTT9tVtmqMYT5f2JiRlWYPawc2ehDZS3BMDNoFr3pKpLcN5h6OScf-NZI7oTRgWUu968RqpZKsILyPcu9BCCq1A",
    model_kwargs={
        "model": "mixtral-8x7b-instruct-fp16",
        "max_tokens": 128,
        "presence_penalty": 0,
        "temperature": 0.01,
        "top_p": 0.9,
        "messages": [
            {
                "role": "system",
                "content": """
Reply with a PURE JSON response. Do not include any other text in your response. Include only correct JSON.
The keys to your response should be the names of the <input> and <textarea> elements in the form. The values should be the user's input for each element, given their prompt.
""",
            },
        ],
    },
)

# files = os.listdir("./data")
# file_texts = []
# for file in files:
#     with open(f"./data/{file}") as f:
#         file_text = f.read()
#     text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#         chunk_size=512,
#         chunk_overlap=64,
#     )
#     texts = text_splitter.split_text(file_text)
#     for i, chunked_text in enumerate(texts):
#         file_texts.append(
#             Document(
#                 page_content=chunked_text,
#                 metadata={"doc_title": file.split(".")[0], "chunk_num": i},
#             )
#         )


# vector_store = Milvus.from_documents(
#     file_texts,
#     embedding=embeddings,
#     connection_args={"host": "localhost", "port": 19530},
#     collection_name="cities",
# )

# file_texts[0]


# template = """Answer the question based only on the following context:
# {context}

# Question: {question}
# """
template = """

Question: {question}
"""
prompt = PromptTemplate.from_template(template)

chain = {"question": RunnablePassthrough()} | prompt | llm | SimpleJsonOutputParser()
