from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def home() -> dict:
    return {"message": "This app is powered by FastAPI-Beanie combo..."}



