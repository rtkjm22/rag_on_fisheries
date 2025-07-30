from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_function():
    return HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-small")


# model = SentenceTransformer("cl-tohoku/bert-base-japanese-whole-word-masking")


# def embed(text: str) -> list[float]:
#     return model.encode(text).tolist()
