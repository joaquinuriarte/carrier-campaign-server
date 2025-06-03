from fastapi import FastAPI, Depends
import uvicorn
from app.api import loads, calculations
from app.security import get_api_key

app = FastAPI(
    title="Carrier Campaign Server",
    description="API for carrier campaign calculations with API key authentication and load retrieval",
    version="1.0.0"
)

# Include routers with API key dependency
app.include_router(loads.router, dependencies=[Depends(get_api_key)])
app.include_router(calculations.router, dependencies=[Depends(get_api_key)])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 