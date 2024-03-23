from langchain_community.embeddings import OctoAIEmbeddings

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.octoai_endpoint import OctoAIEndpoint
from langchain_community.vectorstores import Milvus
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_community.llms.octoai_endpoint import OctoAIEndpoint

import os


load_dotenv()
os.environ["OCTOAI_API_TOKEN"] = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiJiMjA2Zjk4OS01N2JjLTQ2ZGItYmVkYi05MTNiMGIxODMzYzgiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiI4ZjM3NzEwMi03ZDM0LTQ5MTktOTQ2Ni04OTYxMTM5MzFkOWEiLCJ1c2VySWQiOiJiYjBmZGU0My1hY2NkLTQ5ZjMtYmM0YS0yYTBiNzNlM2M5ZTAiLCJyb2xlcyI6WyJGRVRDSC1ST0xFUy1CWS1BUEkiXSwicGVybWlzc2lvbnMiOlsiRkVUQ0gtUEVSTUlTU0lPTlMtQlktQVBJIl0sImF1ZCI6IjNkMjMzOTQ5LWEyZmItNGFiMC1iN2VjLTQ2ZjYyNTVjNTEwZSIsImlzcyI6Imh0dHBzOi8vaWRlbnRpdHkub2N0b21sLmFpIiwiaWF0IjoxNzExMjExODAxfQ.GaaXvPGgp40CT5r-PTzaOoIHm28VTkx49utRAar6xIbu2vaduQya3IoodjxuwkWpLmwRDZzxO6yzmkD69KvN9_R0PcIwPSmg01DARubTmvbzPFMPzynbvdJrN27sNrjaxdJBYahL9vkI4Jr7lbuihy79-TpOHtQVwta0HfsNcHZPHD-P6pm4gPjN6U_9TpbaPJFDBeOFHzCXsX8-yhihT6apfo8PKZMZiNi257WrC8TTBqYA6yLeRP8hmtEv1GVHTT9tVtmqMYT5f2JiRlWYPawc2ehDZS3BMDNoFr3pKpLcN5h6OScf-NZI7oTRgWUu968RqpZKsILyPcu9BCCq1A"
)
embeddings = OctoAIEmbeddings(endpoint_url="https://text.octoai.run/v1/embeddings")
# print("EMBEDDREADCHED")
# files = os.listdir("./data")
# file_texts = []
# print("2EMBEDDREADCHED")

# for file in files:
#     with open(f"./data/{file}") as f:
#         file_text = f.read()
#     text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#         separator="\n",
#         chunk_size=128,
#         chunk_overlap=32,
#     )
#     texts = text_splitter.split_text(file_text)
#     for i, chunked_text in enumerate(texts):
#         file_texts.append(
#             Document(
#                 page_content=chunked_text,
#                 metadata={"doc_title": file.split(".")[0], "chunk_num": i},
#             )
#         )

print("EMBEDDREADCHED3")

vector_store = Milvus(
    # file_texts,
    embeddings,
    connection_args={"host": "localhost", "port": 19530},
    collection_name="examples",
)
print("EMBEDDREADCHED4")

# file_texts[0]

retriever = vector_store.as_retriever()
