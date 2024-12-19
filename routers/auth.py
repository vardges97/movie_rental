from fastapi import APIRouter, HTTPException

from models.schemes import User, LoginRequest
from utils.auth_utils import create_jwt_token


router = APIRouter()

users_db = {}

@router.post("/register")
def register_form(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = {"email": user.email, "password": user.password}
    return {"message": "User Registered"}

@router.post("/login")
def login_form(request: LoginRequest):
    user = users_db.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    token = create_jwt_token({"sub": request.username})
    return {"access_token": token}