# cast-service/app/api/casts.py

from fastapi import Header, APIRouter, HTTPException
from typing import List

from app.api.models import CastIn, CastOut, CastUpdate
from app.api import db_manager
from app.api.utils import trace

casts = APIRouter()

@trace
@casts.get('/', response_model=List[CastOut])
async def index():
    return await db_manager.get_all_casts()

@trace
@casts.post('/', status_code=201)
async def add_cast(payload: CastIn):
    cast_id = await db_manager.add_cast(payload)
    response = {
        "id": cast_id,
        **payload.dict(),
    }
    return response

@trace
@casts.get('/{id}', response_model=CastOut)
async def get_cast(id: int):
    cast = await db_manager.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast with given id is not found")
    return cast

@trace
@casts.put('/{id}', status_code=204)
async def update_cast(id: int, payload: CastUpdate):
    cast = await db_manager.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast with given id is not found")
    update_data = payload.dict(exclude_unset=True)
    cast_in_db = CastUpdate(**cast)
    update_cast = cast_in_db.copy(update=update_data)
    return await db_manager.update_cast(id, update_cast)

@trace
@casts.delete('/{id}', status_code=200)
async def delete_cast(id: int):
    cast = await db_manager.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detal="Cast with given id is not found")
    return await db_manager.delete_cast(id) 