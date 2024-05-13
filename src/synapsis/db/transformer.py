from datetime import datetime


def format_data(
    id_karyawan: int, nama_karyawan: str, kondisi: str, terupdate: datetime
):
    return {
        "id_karyawan": id_karyawan,
        "nama_karyawan": nama_karyawan,
        "kondisi": kondisi,
        "terupdate": terupdate,
    }
