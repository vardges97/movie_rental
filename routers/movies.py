from fastapi import APIRouter, Depends, Query

from models.schemes import Movie
from utils.auth_utils import get_current_user

router = APIRouter()

movies_db = []

@router.get("/movies")
def get_movies(genre: str = Query(None, description="Filter by genre"), rating: float = Query(None, description="Filter by rating")):
    filtered_movies = movies_db
    if genre:
        filtered_movies = [movie for movie in filtered_movies if movie.genre == genre]
    if rating:
        filtered_movies = [movie for movie in filtered_movies if movie.rating == rating]
    return filtered_movies

@router.post("/movies")
def add_movie(movie: Movie, current_user: dict = Depends(get_current_user)):
    movies_db.append(movie)
    return {"message": "Movie added successfully"}