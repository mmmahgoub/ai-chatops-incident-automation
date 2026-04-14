from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="AI ChatOps Incident Automation")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "ChatOps AI is running"}