from beanie import pydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models.product_review import ProductReview, UpdateProductReview

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
async def get_product_review(id: pydanticObjectId) -> ProductReview:
    review = await ProductReview.get(id)
    return review

@router.put("/{id}", response_description="Review record updated in the database")
async def update_product_review(id: pydanticObjectId, req: UpdateProductReview) -> ProductReview:
    req = {k:v for k,v in req.dict().items() if v is not None}
    update_query = { "$set": {
            field: value for field, value in req.items()
        }
    }

    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review record not found!")
    
    await review.update(update_query)
    return review

@router.delete("/{id}", response_description="Review record deleted in the database")
async def delete_product_review(id: pydanticObjectId) -> dict:
    review = await ProductReview.get(id)

    if not review:
        raise HTTPException(status_code=404, detail="Review record not found!")
    
    await review.delete()
    return {"message": "Review deleted successfully!"}
