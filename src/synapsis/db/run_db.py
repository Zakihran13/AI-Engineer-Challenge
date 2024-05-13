import db.entities as entities
from db import client


async def init_timescale_db():
    db = client.init_async_db()
    
    async with db.begin() as conn:
        await conn.run_sync(entities.meta.create_all)
