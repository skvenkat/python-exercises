import os
from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.product_review import ProductReview

async def init_db():
    client = db.motor_asyncio.AsyncIOMotorClient(os.environ["DATABASE_URI"])
    await init_beanie(database=client.db_name, document_models=[ProductReview])

