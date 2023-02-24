# app/main.py

from fastapi import FastAPI
from app.db import database, User

app = FastAPI(title="FastAPI, Docker, Treafik")

@app.get("/")
async def read_root():
    return await User.objects.all()

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()