from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class CallDataBase(BaseModel):
    call_date: Optional[datetime] = Field(None, nullable=True)
    base_price: Optional[float] = Field(None, ge=0, nullable=True)
    final_price: Optional[float] = Field(None, ge=0, nullable=True)
    load_origin: Optional[str] = Field(None, max_length=100, nullable=True)
    call_outcome: Optional[str] = Field(None, max_length=50, nullable=True)
    call_duration: Optional[int] = Field(None, ge=0, nullable=True)  # Duration in seconds
    is_negotiated: Optional[bool] = Field(None, nullable=True)
    load_destination: Optional[str] = Field(None, max_length=100, nullable=True)
    carrier_sentiment: Optional[str] = Field(None, max_length=50, nullable=True)

    ## TODO: Add validation for the data using the validator (We could ensure the classifiers respected the tags)
