from beanie import pydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.product_review import ProductReview, UpdateProductReview

router = APIRouter()

@router.post("/", response_description="Review added to the database")
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {"message": "Review added successfully!"}

@router.get("/", response_description="Review records fetched from database")
async def get_product_reviews() -> List(ProductReview):
    reviews = await ProductReview.find_all().to_list()
    return reviews

@router.get("/{id}", response_description="Review record fetched from database")
async def get_product_review(id) -> ProductReview:
    review = await ProductReview.get(id)
    return review




