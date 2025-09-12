from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

class Book(SQLModel, table=True):
    __tablename__ = "books" # type: ignore

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime = Field(default=datetime.now(), sa_column=Column(pg.TIMESTAMP))
    updated_at: datetime = Field(default=datetime.now(), sa_column=Column(pg.TIMESTAMP))

    def __repr__(self) -> str:
        return f"<Book {self.title}>"