import os
from beanie import init_beanie
import motor.motor_asyncio

from app.api.models.product_review import ProductReview

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URI"])
    await init_beanie(database=client.db_name, document_models=[ProductReview])
