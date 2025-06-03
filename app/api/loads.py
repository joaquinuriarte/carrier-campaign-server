from fastapi import APIRouter
from typing import List, Dict, Any
from app.data.loads import LOADS

router = APIRouter(prefix="/loads", tags=["loads"])

@router.get("/", response_model=List[Dict[str, Any]])
async def get_loads():
    """
    Returns a list of available loads
    """
    return LOADS 