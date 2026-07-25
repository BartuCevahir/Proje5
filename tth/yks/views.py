from django.shortcuts import render

from .models import (
    say_puan_model,
    say_siralama_model,
    ea_puan_model,
    ea_siralama_model,
    soz_puan_model,
    soz_siralama_model,
)


def anasayfa(request):

    puan = None
    siralama = None

    if request.method == "POST":

        puan_turu = request.POST.get("puan_turu")

        dersler = [
            "turkce",
            "matematik",
            "sosyal",
            "fen",
            "ayt_matematik",
            "fizik",
            "kimya",
            "biyoloji",
            "edebiyat",
            "tarih1",
            "cografya1",
            "tarih2",
            "cografya2",
            "felsefe",
            "din",
        ]

        netler = {}

        for ders in dersler:

            dogru = float(request.POST.get(f"{ders}_dogru") or 0)
            yanlis = float(request.POST.get(f"{ders}_yanlis") or 0)

            net = dogru - (yanlis / 4)

            netler[ders] = net

        obp = float(request.POST.get("obp") or 0)

        bos_mu = all(net == 0 for net in netler)

        if bos_mu:
            return render(request,"yks.html",
        {
            "hata": "Lütfen notlarınızı giriniz."
        },
    )

        # SAYISAL

        if puan_turu == "say":

            veri = [[
                netler["turkce"],
                netler["matematik"],
                netler["sosyal"],
                netler["fen"],
                netler["ayt_matematik"],
                netler["fizik"],
                netler["kimya"],
                netler["biyoloji"],
                obp,
            ]]

            puan = say_puan_model.predict(veri)[0]
            siralama = say_siralama_model.predict(veri)[0]

        # EŞİT AĞIRLIK

        elif puan_turu == "ea":

            veri = [[
                netler["turkce"],
                netler["matematik"],
                netler["sosyal"],
                netler["fen"],
                netler["ayt_matematik"],
                netler["edebiyat"],
                netler["tarih1"],
                netler["cografya1"],
                obp,
            ]]

            puan = ea_puan_model.predict(veri)[0]
            siralama = ea_siralama_model.predict(veri)[0]

        # SÖZEL

        else:

            veri = [[
                netler["turkce"],
                netler["matematik"],
                netler["sosyal"],
                netler["fen"],
                netler["edebiyat"],
                netler["tarih1"],
                netler["cografya1"],
                netler["tarih2"],
                netler["cografya2"],
                netler["felsefe"],
                netler["din"],
                obp,
            ]]

            puan = soz_puan_model.predict(veri)[0]
            siralama = soz_siralama_model.predict(veri)[0]

        puan = round(float(puan), 2)
        siralama = max(1, int(siralama))

        print("Puan:", puan)
        print("Sıralama:", siralama)

    return render(
        request,
        "yks.html",
        {
            "puan": puan,
            "siralama": siralama,
        },
    )



# from django.shortcuts import render
# from .models import *


# def anasayfa(request):

#     puan = None
#     siralama = None

#     if request.method == "POST":

#         puan_turu = request.POST.get("puan_turu")

#         dersler = [
#             "turkce",
#             "matematik",
#             "sosyal",
#             "fen",
#             "ayt_matematik",
#             "fizik",
#             "kimya",
#             "biyoloji",
#             "edebiyat",
#             "tarih1",
#             "cografya1",
#             "tarih2",
#             "cografya2",
#             "felsefe",
#             "din",
#         ]

#         netler = []

#         for ders in dersler:

#             dogru = request.POST.get(f"{ders}_dogru")
#             yanlis = request.POST.get(f"{ders}_yanlis")

#             if dogru == "" and yanlis == "":

#                 net = 0

#             else:

#                 dogru = float(dogru or 0)
#                 yanlis = float(yanlis or 0)

#                 net = dogru - (yanlis / 4)

#             netler.append(net)

#         if puan_turu == "say":

#             katsayilar = [
#                 1.3, 1.3, 1.3, 1.3,
#                 3.0, 2.8, 2.8, 2.8,
#                 0, 0, 0,
#                 0, 0, 0, 0
#             ]

#         elif puan_turu == "ea":

#             katsayilar = [
#                 1.3, 1.3, 1.3, 1.3,
#                 2.5, 0, 0, 0,
#                 2.5, 2.0, 1.5,
#                 0, 0, 0, 0
#             ]

#         else:

#             katsayilar = [
#                 1.3, 1.3, 1.3, 1.3,
#                 0, 0, 0, 0,
#                 2.8, 2.4, 2.0,
#                 2.4, 2.0, 2.0, 1.5
#             ]

#         puan = 100

#         for net, katsayi in zip(netler, katsayilar):

#             puan += net * katsayi

#         puan = round(puan, 2)

#         siralama = int(3000000 * (560 / puan) ** 3)

#         if siralama < 1:

#             siralama = 1

#     print("Puan:", puan)
#     print("Sıralama:", siralama)
#     print("Netler:", netler)



#     return render(
#         request,
#         "yks.html",
#         {
#             "puan": puan,
#             "siralama": siralama,
#         },
#     )











# from django.shortcuts import render





# # from .yks_models import puan_model, siralama_model
# from .models import puan_model, siralama_model


# def anasayfa(request):

#     tahmini_puan = None
#     tahmini_siralama = None

#     if request.method == "POST":
#         puan_turu = request.POST.get("puan_turu")

#         dersler = [
#     "turkce",
#     "matematik",
#     "sosyal",
#     "fen",
#     "ayt_matematik",
#     "fizik",
#     "kimya",
#     "biyoloji",
#     "edebiyat",
#     "tarih1",
#     "cografya1",
#     "tarih2",
#     "cografya2",
#     "felsefe",
#     "din",
# ]

# netler = []

# for ders in dersler:

#     dogru = request.POST.get(f"{ders}_dogru")
#     yanlis = request.POST.get(f"{ders}_yanlis")

#     if dogru == "" and yanlis == "":
#         net = 0

#     else:
#         dogru = float(dogru or 0)
#         yanlis = float(yanlis or 0)

#         net = dogru - (yanlis / 4)

#     netler.append(net)


# if puan_turu == "say":

#     katsayilar = [
#         1.3, 1.3, 1.3, 1.3,
#         3.0, 2.8, 2.8, 2.8,
#         0, 0, 0,
#         0, 0, 0, 0
#     ]

# elif puan_turu == "ea":

#     katsayilar = [
#         1.3, 1.3, 1.3, 1.3,
#         2.5, 0, 0, 0,
#         2.5, 2.0, 1.5,
#         0, 0, 0, 0
#     ]

# else:

#     katsayilar = [
#         1.3, 1.3, 1.3, 1.3,
#         0, 0, 0, 0,
#         2.8, 2.4, 2.0,
#         2.4, 2.0, 2.0, 1.5
#     ]





#     puan = 100

# for net, katsayi in zip(netler, katsayilar):
#     puan += net * katsayi



#     siralama = int(3000000 * (560 / puan) ** 3)

# if siralama < 1:
#     siralama = 1    



# def anasayfa(request):

#     puan = None
#     siralama = None

#     if request.method == "POST":

#         # bütün hesaplamalar burada

#         puan = 450
#         siralama = 25000

#     return render(
#         request,
#         "yks.html",
#         {
#             "puan": puan,
#             "siralama": siralama,
#         },
#     )









    #     veriler = [[
    #         float(request.POST.get("turkce_tyt") or 0),
    #         float(request.POST.get("matematik_tyt") or 0),
    #         float(request.POST.get("sosyal_tyt") or 0),
    #         float(request.POST.get("fen_tyt") or 0),
    #         float(request.POST.get("matematik_ayt") or 0),
    #         float(request.POST.get("fizik_ayt") or 0),
    #         float(request.POST.get("kimya_ayt") or 0),
    #         float(request.POST.get("biyoloji_ayt") or 0),
    #     ]]

    #     tahmini_puan = round(
    #         puan_model.predict(veriler)[0],
    #         2
    #     )

    #     tahmini_siralama = int(
    #         siralama_model.predict(veriler)[0]
    #     )

    # return render(
    #     request,
    #     "yks.html",   
    #     {
    #         "tahmini_puan": tahmini_puan,
    #         "tahmini_siralama": tahmini_siralama,
    #     }
    # )