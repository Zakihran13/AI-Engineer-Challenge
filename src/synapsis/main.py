from fastapi import FastAPI, Body
from typing import Optional
from loguru import logger
import asyncio

from synapsis.system import routine_predict
from synapsis.db import run_db

app = FastAPI()


@app.post("/start_inferencing")
async def start_inferencing(data: dict = Body(...)):
    """Initiate inference process"""
    source_dir = data.get('source_dir')
    id_karyawan = data.get('id_karyawan')
    nama_karyawan = data.get('nama_karyawan')

    if not all([source_dir, id_karyawan, nama_karyawan]):
        return {"error": "Missing required parameters"}

    logger.info("Initiating inference process!")
    try:
        # Replace with actual implementation
        res = await routine_predict.exec_routine(source_dir, id_karyawan, nama_karyawan)
        return {"result": res}
    except Exception as e:
        logger.error(f"Error during inference process: {e}")
        return {"error": str(e)}


@app.post("/start_db")
async def start_db():
    """Initialize TimescaleDB schema"""
    logger.info("Initializing TimescaleDB schema")
    try:
        await run_db.init_timescale_db()
        return {"message": "Schema created successfully!"}
    except Exception as e:
        logger.warning(f"Failed to initialize schema: {e}")
        return {"error": str(e)}

