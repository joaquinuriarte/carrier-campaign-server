from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/calculations", tags=["calculations"])

class PriceNegotiationRequest(BaseModel):
    base_price: str
    negotiated_price: str

@router.post("/percentage")
async def calculate_percentage(request: PriceNegotiationRequest):
    """
    Calculates the percentage increase between base price and negotiated price.
    Accepts both values as strings and converts them to floats.
    Returns the percentage increase.
    """
    try:
        base_price = float(request.base_price)
        negotiated_price = float(request.negotiated_price)

        if base_price <= 0:
            raise HTTPException(status_code=400, detail="Base price must be greater than zero")
        if negotiated_price <= 0:
            raise HTTPException(status_code=400, detail="Negotiated price must be greater than zero")

        percentage_increase = ((negotiated_price - base_price) / base_price) * 100

        return {
            "base_price": base_price,
            "negotiated_price": negotiated_price,
            "percentage_increase": round(percentage_increase, 2),
            "message": f"Price {'increased' if percentage_increase > 0 else 'decreased'} by {abs(round(percentage_increase, 2))}%"
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Both base_price and negotiated_price must be valid numbers.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 