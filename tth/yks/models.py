import pandas as pd
from sklearn.linear_model import LinearRegression

# veri = pd.read_csv("yks_veri_seti_400_plus.csv")

import os

BASE_DIR = os.path.dirname(__file__)

csv_yolu = os.path.join(
    BASE_DIR,
    "yks_veri_seti_400_plus.csv"
)

veri = pd.read_csv(csv_yolu)




# SAY

say_veri = veri[veri["puan_turu"] == "SAY"]

X_say = say_veri[
    [
        "tyt_turkce",
        "tyt_matematik",
        "tyt_sosyal",
        "tyt_fen",
        "ayt_matematik",
        "ayt_fizik",
        "ayt_kimya",
        "ayt_biyoloji",
        "obp",
    ]
]

say_puan_model = LinearRegression()
say_puan_model.fit(X_say, say_veri["yks_puan"])

say_siralama_model = LinearRegression()
say_siralama_model.fit(X_say, say_veri["siralama"])


# EA

ea_veri = veri[veri["puan_turu"] == "EA"]

X_ea = ea_veri[
    [
        "tyt_turkce",
        "tyt_matematik",
        "tyt_sosyal",
        "tyt_fen",
        "ayt_matematik",
        "ayt_tded",
        "ayt_tarih1",
        "ayt_cografya1",
        "obp",
    ]
]

ea_puan_model = LinearRegression()
ea_puan_model.fit(X_ea, ea_veri["yks_puan"])

ea_siralama_model = LinearRegression()
ea_siralama_model.fit(X_ea, ea_veri["siralama"])


# SÖZ

soz_veri = veri[veri["puan_turu"] == "SÖZ"]

X_soz = soz_veri[
    [
        "tyt_turkce",
        "tyt_matematik",
        "tyt_sosyal",
        "tyt_fen",
        "ayt_tded",
        "ayt_tarih1",
        "ayt_cografya1",
        "ayt_tarih2",
        "ayt_cografya2",
        "ayt_felsefe",
        "ayt_din",
        "obp",
    ]
]

soz_puan_model = LinearRegression()
soz_puan_model.fit(X_soz, soz_veri["yks_puan"])

soz_siralama_model = LinearRegression()
soz_siralama_model.fit(X_soz, soz_veri["siralama"])




# from django.db import models

# # Create your models here.
# from sklearn.linear_model import LinearRegression
# import numpy as np

# X = np.array([
#     [35, 30, 18, 17, 35, 12, 10, 11],
#     [30, 25, 15, 15, 28, 8, 7, 8],
#     [40, 38, 20, 20, 38, 14, 13, 13],
#     [25, 20, 10, 10, 20, 5, 4, 5],
#     [20, 15, 8, 7, 15, 3, 3, 2],
#     [37, 35, 19, 18, 36, 13, 12, 12],
# ])

# puanlar = np.array([
#     495,
#     420,
#     540,
#     330,
#     280,
#     515,
# ])

# siralamalar = np.array([
#     1000,
#     50000,
#     200,
#     180000,
#     350000,
#     5000,
# ])

# puan_model = LinearRegression()
# puan_model.fit(X, puanlar)

# siralama_model = LinearRegression()
# siralama_model.fit(X, siralamalar)