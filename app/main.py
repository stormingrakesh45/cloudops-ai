from fastapi import FastAPI
from app.api.logs import router as logs_router

app = FastAPI(title="CloudOps AI")

app.include_router(logs_router)

@app.get("/health")
def health_check():
    return {"status": "x"}
