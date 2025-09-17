# Inside main.py title
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

from src.db.main import init_db

version = "v1"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    print("server is stopping")


app = FastAPI(
    lifespan=lifespan,
    title="Bookly",
    description="A RESTful API for a book review web service",
    version=version,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
