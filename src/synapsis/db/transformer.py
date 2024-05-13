from datetime import datetime


def format_data(
    id_karyawan: int, nama_karyawan: str, kondisi: str, terupdate: datetime
):
    return {
        "id_karyawan": int(id_karyawan),
        "nama_karyawan": nama_karyawan,
        "kondisi_terakhir": kondisi,
        "terakhir_update": terupdate,
    }
