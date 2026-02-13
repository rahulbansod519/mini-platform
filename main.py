import os
from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

@app.get("/")

def root():
    return {
        "message": "Welcome to the FastAPI application!",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
def health_check():
    return {
        "status": "unhealthy",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/ready")
def readiness_check():
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat()
    }
    

@app.get("/info")
def info():
    return {
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    }