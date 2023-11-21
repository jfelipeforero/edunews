from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from models.query import Base as BaseMigration
# from core.config import settings

"""
The entire project make use of async operations(asyncio) throught the entire
project which allows better performance overall
"""
DB_URL = "postgresql+asyncpg://jfelipef:password@postgres_query:5432/query"
async_engine = create_async_engine(DB_URL, future=True, echo=True)
AsyncSessionFactory = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

async def create_all_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(BaseMigration.metadata.create_all)
 
