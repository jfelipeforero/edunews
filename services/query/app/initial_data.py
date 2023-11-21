import logging
import asyncio

from db_config.init_db import migrate_db
from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def init() -> None:  
    await migrate_db(settings.MIGRATIONS_DATABASE_URL)

async def main() -> None:
    logger.info("Creating initial data")
    await init()
    logger.info("Initial data created")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
