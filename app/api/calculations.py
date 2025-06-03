from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/calculations", tags=["calculations"])

class PriceNegotiationRequest(BaseModel):
    base_price: float
    negotiated_price: float

@router.post("/percentage")
async def calculate_percentage(request: PriceNegotiationRequest):
    """
    Calculates the percentage increase between base price and negotiated price.
    Returns the percentage increase.
    """
    try:
        if request.base_price <= 0:
            raise HTTPException(status_code=400, detail="Base price must be greater than zero")
        
        if request.negotiated_price <= 0:
            raise HTTPException(status_code=400, detail="Negotiated price must be greater than zero")
        
        percentage_increase = ((request.negotiated_price - request.base_price) / request.base_price) * 100
        
        return {
            "base_price": request.base_price,
            "negotiated_price": request.negotiated_price,
            "percentage_increase": round(percentage_increase, 2),
            "message": f"Price {'increased' if percentage_increase > 0 else 'decreased'} by {abs(round(percentage_increase, 2))}%"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 