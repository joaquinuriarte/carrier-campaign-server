from fastapi import APIRouter
from app.models.schemas import CallDataBase

router = APIRouter(prefix="/data", tags=["data"])

@router.post("/ingest")
async def ingest_data(request: CallDataBase):
    """
    Endpoint to ingest call data. Validates input and prints to console for now.
    """
    print("Received call data:", request.dict())
    return {"message": "Data received and validated successfully."}