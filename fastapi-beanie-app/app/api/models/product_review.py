from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional

class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "product_review"

    class Config:
        schema_extra = {
            "example": {
                "name": "Apple Iphone 14",
                "product": "mobile phone",
                "rating": 4.5,
                "review": "Always unbeatable.",
                "date": datetime.now(),
            }
        }

class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "name": "Apple Iphone 14",
                "product": "mobile phone",
                "rating": 4.8,
                "review": "Always unbeatable and top-notch in quality.",
                "date": datetime.now(),
            }
        }