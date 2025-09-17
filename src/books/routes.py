from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, BookCreateModel, BookUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession

from src.books.service import BookService
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    """Lấy tất cả sách từ database"""
    books = await book_service.get_all_books(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session)
):
    """Tạo một cuốn sách mới trong database"""
    new_book = await book_service.create_book(book_data, session)
    return new_book


@book_router.get("/{book_uid}", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    """Lấy một cuốn sách theo UID"""
    book = await book_service.get_book_by_uid(book_uid, session)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
):
    """Cập nhật thông tin sách"""
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return updated_book


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    """Xóa một cuốn sách"""
    result = await book_service.delete_book(book_uid, session)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return {}
