# Inside main.py title
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import initdb # Import hàm initdb

version = 'v1'

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await initdb() # Gọi hàm initdb khi server khởi động
    yield
    print("Server is stopping")

app = FastAPI(
    lifespan=lifespan,
    title='Bookly',
    description='A RESTful API for a book review web service',
    version=version,
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])