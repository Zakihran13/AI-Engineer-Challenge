import synapsis.db.entities as entities
from synapsis.db import client

from loguru import logger


async def init_timescale_db():
    db = client.init_async_db()

    try:
        async with db.begin() as conn:
            await conn.run_sync(entities.meta.create_all)
    except Exception as e:
        logger.warning(f"make sure that 'synapsis' schema exist in db! \nerror: {e}")
