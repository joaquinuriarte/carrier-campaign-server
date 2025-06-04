# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Speed & cleanliness
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# If this is FastAPI
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

