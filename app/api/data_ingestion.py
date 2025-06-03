from fastapi import APIRouter, HTTPException
from app.models.schemas import CallDataBase
from app.database.models import CallData
from app.database.connection import SessionLocal

router = APIRouter(prefix="/data", tags=["data"])

@router.post("/ingest")
async def ingest_data(request: CallDataBase):
    """
    Endpoint to ingest call data into the database.
    Uses a single database session for all requests.
    """
    db = SessionLocal()
    try:
        # Create a new CallData instance from the request
        db_call_data = CallData(
            call_date=request.call_date,
            base_price=request.base_price,
            final_price=request.final_price,
            load_origin=request.load_origin,
            call_outcome=request.call_outcome,
            call_duration=request.call_duration,
            is_negotiated=request.is_negotiated,
            load_destination=request.load_destination,
            carrier_sentiment=request.carrier_sentiment
        )
        
        # Add to database session
        db.add(db_call_data)
        db.commit()
        db.refresh(db_call_data)
        
        return {
            "message": "Data ingested successfully",
            "id": db_call_data.id
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error ingesting data: {str(e)}"
        )
    finally:
        db.close()