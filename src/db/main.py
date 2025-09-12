from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

# Tạo engine để kết nối CSDL
engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL, # Lấy URL từ file config
    echo=True # Log các câu lệnh SQL ra terminal
))

async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        statement = text("select 'Hello World'")

        result = await conn.execute(statement)

        print(result)