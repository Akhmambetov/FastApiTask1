from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///power_stations.db", echo=True)

new_async_session = async_sessionmaker(engine, expire_on_commit = False)

class Base(DeclarativeBase):
    pass

async def get_session():
    async with new_async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]