# Carrier Campaign Server

A FastAPI-based server for managing carrier campaign calculations and data. Secured with API key authentication and deployed on Render.

## Overview

The server provides three main endpoints:
- Load data retrieval: Used by agent to get available loads
- Load price calculations: Used by agent to handle price negotiations
- Call data ingestion: Used by agent to add call_data produced by the call to the database

All endpoints require API key authentication via the `X-API-Key` header and are served over HTTPS.

## Components

- **API Layer**: FastAPI application with three main routers (loads, calculations, data ingestion)
- **Security**: API key validation using environment variables
- **Database**: Managing connection with PostgreSQL database for storing call data
- **Scripts**: Utilities for API key generation and table creation
- **Data**: Sample loads for demo purposes
- **Models**: Pydantic models for request/response validation and SQLAlchemy models for database operations

## Deployment

### API Key Setup
1. Generate API key using the script:
```bash
python scripts/generate_api_key.py
```
2. Store the generated key:
   - Local: Add to docker run command: `-e API_KEY="your_generated_key"`
   - Production: Add to Render environment variables (key: API_KEY)

### Local Development
1. Install Docker
2. Build and run:
```bash
docker build -t carrier-campaign-server .
docker run -p 8000:8000 -e DATABASE_URL="your_db_url" -e API_KEY="your_generated_key" carrier-campaign-server
```

### Render Deployment
1. Fork this repository
2. Create a new Web Service on Render
3. Connect to your GitHub repository
4. Add environment variables:
   - DATABASE_URL: Your PostgreSQL URL
   - API_KEY: Your generated API key
5. Render will automatically detect the Dockerfile and deploy

### Database Setup
- Create a PostgreSQL database on Render
- Add the database URL to the Web Service's environment variables (Use key_name: DATABASE_URL)
- The server will automatically connect using the provided URL

## Accessing Deployment: API Endpoints

### Get Loads
```http
GET https://carrier-campaign-server-docker.onrender.com/loads
Header: X-API-Key: your_api_key
```

### Calculate Percentage
```http
POST https://carrier-campaign-server-docker.onrender.com/calculations/percentage
Header: X-API-Key: your_api_key
```

Request body:
```json
{
    "base_price": "750",
    "negotiated_price": "850"
}
```

### Ingest Call Data
```http
POST https://carrier-campaign-server-docker.onrender.com/data/ingest
Header: X-API-Key: your_api_key
```

Request body:
```json
{
    "call_date": "2025-05-04T20:13:08.554+0000",
    "base_price": "990",
    "final_price": "1020",
    "load_origin": "Miami",
    "call_outcome": "success_rate_booked",
    "call_duration": "190",
    "is_negotiated": "true",
    "load_destination": "Seattle",
    "carrier_sentiment": "carrier_sentiment_negative"
}
```

> Note: The deployed instance on Render's free tier may take a few moments to spin up after periods of inactivity.
