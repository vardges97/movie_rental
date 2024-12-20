from typing import Dict
from fastapi import APIRouter, Depends

from models.schemes import Rental
from utils.auth_utils import get_current_user


router = APIRouter()

rentals_db = []

@router.get("/")
def get_rental_history(current_user: Dict = Depends(get_current_user)):
    user_rentals = [rental for rental in rentals_db if rental.user == current_user["username"]]
    return user_rentals


@router.post("/")
def rent_movie(rental: Rental, current_user = Depends(get_current_user)):
    rentals_db.append(rental)
    return {"message": "Movie rented"}