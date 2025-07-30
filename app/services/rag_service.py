from app.models.db import DATABASE_URL
from langchain.vectorstores.pgvector import PGVector
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


def generate_answer(query: str) -> str:
    embedding_func = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-small",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    retriever = PGVector(
        connection_string=DATABASE_URL,
        collection_name="fisheries",
        embedding_function=embedding_func,
    ).as_retriever(search_kwargs={"k": 3})

    # llm = HuggingFaceHub(
    #     repo_id="rinna/japanese-gpt-neox-3.6b-instruction-ppo",
    #     model_kwargs={"temperature": 0.7, "max_new_tokens": 512},
    # )

    # chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    # return chain.run(query)
