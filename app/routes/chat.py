from fastapi import APIRouter
from app.services.incident import handle_query

router = APIRouter()

@router.post("/chat")
async def chat(query: str):
    response = handle_query(query)
    return {"response": response}