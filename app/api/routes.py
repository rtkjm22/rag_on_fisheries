from fastapi import APIRouter, Query
from app.services.rag_service import generate_answer

router = APIRouter()


@router.get("/ask")
def ask(q: str = Query(..., description="質問文")):
    answer = generate_answer(q)
    return {"question": q, "answer": answer}
