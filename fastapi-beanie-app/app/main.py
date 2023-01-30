from fastapi import FastAPI

from app.api.routes.product_review import router
from app.api.db import init_db


app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def home() -> dict:
    return {"message": "This app is powered by FastAPI-Beanie combo..."}

app.include_router(router, prefix="/api/v1/reviews", tags=["reviews"])
