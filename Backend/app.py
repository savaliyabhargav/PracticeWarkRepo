import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    app_name: str = "Cuisinsta-Backend"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

class Reel(BaseModel):
    id: str
    username: str
    likes: int
    views: int
    shares: int

# Mock Database (20 Reels)
MOCK_REELS = [
    {"id": f"vid_{i}", "username": f"user_{i%5}", "likes": 100 * i, "views": 1000 * i, "shares": 10 * i}
    for i in range(1, 21)
]

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health_check():
    return {"status": "online"}

@app.get("/reels", response_model=List[Reel])
def get_reels(page: int = Query(1, ge=1)):
    page_size = 5
    start = (page - 1) * page_size
    end = start + page_size
    return MOCK_REELS[start:end]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)