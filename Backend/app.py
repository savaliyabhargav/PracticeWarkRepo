import uvicorn
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Configuration - Simplest version
class Settings(BaseSettings):
    app_name: str = "FastAPI Static Service"
    
    # extra="ignore" allows us to leave the .env as is
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

# 2. Initialize FastAPI
app = FastAPI(title=settings.app_name)

# 3. Simple Health Check Endpoint (No DB)
@app.get("/health")
def health_check():
    return {
        "status": "online",
        "service": settings.app_name,
        "message": "Service is running without database dependency"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)