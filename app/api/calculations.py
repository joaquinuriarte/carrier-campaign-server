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
    Returns the percentage increase and a proposed new price based on business rules:
    - If negotiated price is within 20% higher than base price, propose middle point
    - Otherwise, propose 5% increase from base price
    """
    try:
        base_price = float(request.base_price.strip())
        negotiated_price = float(request.negotiated_price.strip())

        if base_price <= 0:
            raise HTTPException(status_code=400, detail="Base price must be greater than zero")
        if negotiated_price <= 0:
            raise HTTPException(status_code=400, detail="Negotiated price must be greater than zero")

        # Calculate percentage increase
        percentage_increase = ((negotiated_price - base_price) / base_price) * 100

        # Calculate proposed new price based on business rules
        if percentage_increase > 0 and percentage_increase <= 20:
            # If within 20% higher, propose middle point
            proposed_new_price = (base_price + negotiated_price) / 2
        else:
            # Otherwise, propose 5% increase
            proposed_new_price = base_price * 1.05

        return {
            "base_price": base_price,
            "negotiated_price": negotiated_price,
            "percentage_increase": round(percentage_increase, 2),
            "proposed_new_price": round(proposed_new_price, 2),
            "message": f"Price {'increased' if percentage_increase > 0 else 'decreased'} by {abs(round(percentage_increase, 2))}%"
        }
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Both base_price and negotiated_price must be valid numbers. Provided: base_price='{request.base_price}', negotiated_price='{request.negotiated_price}'"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 