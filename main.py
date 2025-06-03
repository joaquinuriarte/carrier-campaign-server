from fastapi import FastAPI, Depends
import uvicorn
from app.api import loads, calculations, data_ingestion
from app.security import get_api_key
import subprocess
import os
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get environment variables with defaults
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

app = FastAPI(
    title="Carrier Campaign Server",
    description="API for carrier campaign calculations with API key authentication and load retrieval",
    version="1.0.0"
)

# Include routers with API key dependency
app.include_router(loads.router, dependencies=[Depends(get_api_key)])
app.include_router(calculations.router, dependencies=[Depends(get_api_key)])
app.include_router(data_ingestion.router, dependencies=[Depends(get_api_key)])

def run_streamlit():
    """Run the Streamlit dashboard"""
    try:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'app/dashboard/main.py')
        logger.info(f"Starting Streamlit with file: {filename}")
        
        # Ensure the file exists
        if not os.path.exists(filename):
            logger.error(f"Streamlit file not found: {filename}")
            return
            
        # Set environment variables
        env = os.environ.copy()
        env['STREAMLIT_SERVER_HEADLESS'] = 'true'
        env['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
        
        # Run Streamlit in a subprocess
        subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", filename,
            f"--server.port={API_PORT}",
            f"--server.address={API_HOST}",
            "--server.headless=true",
            "--browser.gatherUsageStats=false",
            "--server.baseUrlPath=dashboard"  # This will make Streamlit available at /dashboard
        ], env=env)
        
    except Exception as e:
        logger.error(f"Error starting Streamlit: {str(e)}")

if __name__ == "__main__":
    # Start Streamlit
    run_streamlit()
    logger.info(f"Started Streamlit process at /dashboard")

    # Start FastAPI server
    logger.info(f"Starting FastAPI server on {API_HOST}:{API_PORT}")
    uvicorn.run("main:app", host=API_HOST, port=API_PORT, reload=True) 