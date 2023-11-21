from alembic import command
import os
from alembic.config import Config
from sqlalchemy.ext.asyncio import create_async_engine
from models.query import Base

"""
This is the process required to run migrations asyncronously(asyncio)
"""

config_path = os.path.join(os.getcwd(), 'alembic.ini')

__config_path__ = config_path
 
path = os.path.join(os.getcwd(), "alembic")

__migration_path__ = path

cfg = Config(__config_path__)
cfg.set_main_option("script_location", __migration_path__)


async def migrate_db(conn_url: str):
    async_engine = create_async_engine(conn_url, echo=True)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(__execute_upgrade)


def __execute_upgrade(connection):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head") 

