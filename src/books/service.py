from datetime import datetime
from sqlalchemy import desc
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.models import Book
from src.books.schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select


class BookService:
    async def get_all_books(self, session: AsyncSession):
        """Lấy danh sách tất cả các cuốn sách"""
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        book_data = Book(**book_data_dict)

        session.add(book_data)
        await session.commit()
        await session.refresh(book_data)
        return book_data

    async def get_book_by_uid(self, book_uid: str, session: AsyncSession):
        """Lấy một cuốn sách bằng uid của nó"""
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None

    async def update_book(
        self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession
    ):
        """Cập nhật một cuốn sách"""
        book_to_update = await self.get_book_by_uid(book_uid, session)

        if book_to_update is not None:
            update_data_dict = update_data.model_dump(exclude_unset=True)
            for key, value in update_data_dict.items():
                setattr(book_to_update, key, value)

            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update
        else:
            return None

    async def delete_book(self, book_uid: str, session: AsyncSession):
        """Xóa một cuốn sách"""
        book_to_delete = await self.get_book_by_uid(book_uid, session)

        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return {}
        else:
            return None
