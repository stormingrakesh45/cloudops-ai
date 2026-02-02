from fastapi import APIRouter
from typing import List
from app.services.anomaly import detect_anomalies

router = APIRouter(
    prefix="/logs",
    tags=["logs"]
)

LOG_STORE = []

@router.post("/ingest")
def ingest_logs(logs: List[str]):
    LOG_STORE.extend(logs)
    return {"message": "logs ingested", "count": len(LOG_STORE)}

@router.get("/analyze/anomaly")
def analyze():
    anomalies = detect_anomalies(LOG_STORE)
    return {"anomalies": anomalies}
