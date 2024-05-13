from ultralytics import YOLO
from os import getenv
from datetime import datetime
from loguru import logger


def kondisi_gambar(source_data: str):
    condition = {
        0: "fatigue",
        1: "unfatigue",
    }

    # import trained model
    trained_model = YOLO(getenv("BEST_MODEL"))

    # predicting the data
    pred_img = trained_model.predict(source_data, conf=0.6)
    
    if not pred_img:
        return

    # getting label output
    label_prediksi = condition[pred_img[0].obb.cls.item()]

    return label_prediksi


# other capabilitie:
# 01. predicting on video
# 02. predicting on streaming camera (real time)
# future improvement if needed