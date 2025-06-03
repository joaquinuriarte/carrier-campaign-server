from fastapi import FastAPI
import uvicorn
from app.api import loads, calculations

app = FastAPI(title="Carrier Campaign Server")

# Include routers
app.include_router(loads.router)
app.include_router(calculations.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 