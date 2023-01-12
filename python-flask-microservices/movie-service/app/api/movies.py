# movie-service/app/main.py

from fastapi import Header, APIRouter
from typing import List

from app.api.models import MovieIn, MovieOut
from app.api import db_manager
from app.api.service import is_cast_present
from api.app.utils import trace

movies = APIRouter()

@trace
@movies.get('/', response_model=List[MovieOut])
async def index():
    return await db_manager.get_all_movies()

@trace
@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail="Cast with given id is not found")

    movie_id = await db_manager.add_movie(payload)
    response = {
        "id": movie_id,
        **payload.dict()
    }
    return response

@trace
@movies.get('/{id}', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id is not found")
    return movie

@trace
@movies.put('/{id}', status_code=204)
async def update_movie(id: int, payload: Movie):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")
    
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail="Cast with given id not found")
    update_data = payload.dict(exclude_unset=True)
    movie_in_db = MovieIn(**movie)
    update_movie = movie_in_db.copy(update=update_data)
    return await db_manager.update_movie(id, update_movie)

@trace
@movies.delete('/{id}', status_code=200)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie with given id not found")

    return await db_manager.delete_movie(id)
