import os
from dotenv import load_dotenv

from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

auth_scheme = OAuth2PasswordBearer(tokenUrl="authorization/login")

def create_jwt_token(data: dict):
    encoding = data.copy()
    encoded_jwt = jwt.encode(encoding, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt_token(token: str):
    try:
        tk = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return tk
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid Token")

def get_current_user(token: str = Depends(auth_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate user",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        tk = verify_jwt_token(token)
        username: str = tk.get("sub")
        if username is None:
            raise credentials_exception
        token_data = {"username": username}
    except JWTError:
        raise credentials_exception
    print(f"Token Data after decode: {token_data}")
    return token_data