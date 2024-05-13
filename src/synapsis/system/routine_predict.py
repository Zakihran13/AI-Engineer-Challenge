from synapsis.system import predict
from synapsis.db import client, transformer, statements as st

from loguru import logger
from datetime import datetime


async def process_image(
    source_data: str, id_karyawan: int, nama_karyawan: str, dt: datetime
):
    predicted_label = predict.kondisi_gambar(source_data)

    if not predicted_label:
        logger.warning("No faces detected! please take a good picture!")
        return

    try:
        async with client.init_async_db().begin() as conn:
            await st.update_db(
                conn=conn,
                data=transformer.format_data(
                    id_karyawan, nama_karyawan, predicted_label, dt
                ),
            )
    except Exception as e:
        logger.warning(f"error while inserting data to db: {e}")

    return {"kondisi": predicted_label, "terakhir_update": dt}


async def exec_routine(source_data: str, id_karyawan: int, nama_karyawan: str):
    dt = datetime.now()

    res = await process_image(source_data, id_karyawan, nama_karyawan, dt)

    if not res:
        return

    return res
