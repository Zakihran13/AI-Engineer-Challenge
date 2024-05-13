import click
import asyncio
from loguru import logger

from src.synapsis.system import routine_predict
from src.synapsis.db import run_db


@click.group()
def cli():
    click.echo("Program Started!")


@cli.command()
@click.argument("source_dir")
@click.argument("id_karyawan")
@click.argument("nama_karyawan")
def start_inferencing(source_dir, id_karyawan, nama_karyawan):
    """mulai memeriksa kondisi karyawan"""
    click.echo("initiating inference proces!")

    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(
        routine_predict.exec_routine(source_dir, id_karyawan, nama_karyawan)
    )

    return res


@cli.command()
def start_db():
    """first time building db schema"""
    click.echo("memulai membuat schema")

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_db.init_timescale_db())
        click.echo("selesai membuat schema!")
    except Exception as e:
        logger.warning(f"failed while building the schema. error: {e}")
