from sqlalchemy import Table, Column, String, Integer, BigInteger, DateTime, MetaData
from datetime import datetime as dt

meta = MetaData(schema="synapsis")

Karyawan = Table(
    "karyawan",
    meta,
    Column("id_karyawan", BigInteger, primary_key=True),
    Column("nama_karyawan", String, primary_key=True),
    Column("bergabung_sejak", DateTime, default=dt.now()),
    Column("terakhir_update", DateTime, onupdate=dt.now()),
    Column("kondisi_terakhir", String),
)
