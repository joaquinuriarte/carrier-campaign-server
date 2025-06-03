from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CallDataBase(BaseModel):
    call_date: Optional[datetime] = None
    base_price: Optional[float] = Field(None, ge=0)
    final_price: Optional[float] = Field(None, ge=0)
    load_origin: Optional[str] = Field(None, max_length=100)
    call_outcome: Optional[str] = Field(None, max_length=50)
    call_duration: Optional[int] = Field(None, ge=0)  # Duration in seconds
    is_negotiated: Optional[bool] = None
    load_destination: Optional[str] = Field(None, max_length=100)
    carrier_sentiment: Optional[str] = Field(None, max_length=50)

    ## TODO: Add validation for the data using the validator (We could ensure the classifiers respected the tags)
