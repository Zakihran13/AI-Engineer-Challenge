from src.synapsis.db import entities as e

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncConnection


async def update_db(conn: AsyncConnection, data: dict):
    if not data:
        return
    
    stmt = insert(e.Karyawan).values(data)
    on_update_stmt = stmt.on_conflict_do_update(
        index_elements=["id_karyawan", "nama_pegawai"],
        set_=dict(stmt.excluded)
    )

    await conn.execute(on_update_stmt)