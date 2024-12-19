import os
import uvicorn
from dotenv import load_dotenv

from fastapi import FastAPI

from routers import auth, movies, rentals


load_dotenv()
PORT = int(os.getenv("PORT"))

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(rentals.router, prefix="/rentals", tags=["Rentals"])


if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True)