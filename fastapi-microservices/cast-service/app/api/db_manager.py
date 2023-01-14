# cast-service/app/api/db_manager.py

from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database

async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.dict())
    return await database.execute_query(query=query)

async def get_all_casts():
    query = casts.select()
    return await database.fetch_all(query=query)

async def get_cast(id: int):
    query = casts.select(casts.c.id==id)
    return await database.fetch_one(query=query)

async def update_cast(id: int, payload: CastUpdate):
    query = casts.update().where(casts.c.id==id).values(**payload.dict())
    return await database.execute(query=query)

async def delete_cast(id: int):
    query = casts.delete().where(casts.c.id==id)
    return await database.execute(query=query)
