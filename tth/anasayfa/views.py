


# from django.shortcuts import render
# from .model import model


# def anasayfa(request):

#     sonuc = None
#     belge = None
#     tahmin = None

#     dersler = [
#         "turkce",
#         "matematik",
#         "fizik",
#         "kimya",
#         "biyoloji",
#         "tarih",
#         "cografya",
#         "felsefe",
#         "ingilizce",
#         "din",
#         "beden",
#         "muzik",
#         "gorsel",
#         "bilgisayar",
#         "psikoloji",
#         "sosyoloji",
#     ]

#     if request.method == "POST":

#         toplam_puan = 0
#         toplam_saat = 0
#         ders_notlari = []

#         for ders in dersler:

#             not_degeri = request.POST.get(f"{ders}_not")
#             saat = request.POST.get(f"{ders}_saat")

#             if not_degeri and saat:

#                 not_degeri = float(not_degeri)
#                 saat = int(saat)

#                 toplam_puan += not_degeri * saat
#                 toplam_saat += saat

#                 ders_notlari.append(not_degeri)

#                 if toplam_saat == 0:

#             belge = "⚠️ Lütfen notları giriniz."
#             tahmin = None

#         else:

#             sonuc = round(toplam_puan / toplam_saat, 2)

#             tahmin = model.predict([[
#                 float(request.POST.get("matematik_not") or 0),
#                 float(request.POST.get("fizik_not") or 0),
#                 float(request.POST.get("kimya_not") or 0),
#                 float(request.POST.get("biyoloji_not") or 0),
#             ]])[0]

#             tahmin = round(tahmin, 2)

#             if any(not_ < 50 for not_ in ders_notlari):

#                 belge = "❌ 50'nin altında notunuz olduğu için belge alamazsınız."

#             elif sonuc >= 85:

#                 belge = "🏆 Takdir Belgesi aldınız."

#             elif sonuc >= 70:

#                 belge = "🎉 Teşekkür Belgesi aldınız."

#             else:

#                 belge = "❌ Belge alamadınız."

#     return render(
#         request,
#         "anasayfa.html",
#         {
#             "sonuc": sonuc,
#             "belge": belge,
#             "tahmin": tahmin,
#         },
#     )
        
        
        
# tahmin = model.predict([[
#     float(request.POST.get("matematik_not") or 0),
#     float(request.POST.get("fizik_not") or 0),
#     float(request.POST.get("kimya_not") or 0),
#     float(request.POST.get("biyoloji_not") or 0),
# ]])[0]

# tahmin = round(tahmin, 2)


from django.shortcuts import render
from .models import models


def anasayfa(request):

    sonuc = None
    belge = None
    tahmin = None

    dersler = [
        "turkce",
        "matematik",
        "fizik",
        "kimya",
        "biyoloji",
        "tarih",
        "cografya",
        "felsefe",
        "ingilizce",
        "din",
        "beden",
        "muzik",
        "gorsel",
        "bilgisayar",
        "psikoloji",
        "sosyoloji",
    ]

    if request.method == "POST":

        toplam_puan = 0
        toplam_saat = 0
        ders_notlari = []

        for ders in dersler:

            not_degeri = request.POST.get(f"{ders}_not")
            saat = request.POST.get(f"{ders}_saat")

            if not_degeri and saat:

                not_degeri = float(not_degeri)
                saat = int(saat)

                toplam_puan += not_degeri * saat
                toplam_saat += saat

                ders_notlari.append(not_degeri)

        if toplam_saat == 0:

            belge = "⚠️ Lütfen notları giriniz."

        else:

            sonuc = round(toplam_puan / toplam_saat, 2)

            

            if any(not_ < 50 for not_ in ders_notlari):

                belge = "❌ 50'nin altında notunuz olduğu için belge alamazsınız."

            elif sonuc >= 85:

                belge = "🏆 Takdir Belgesi aldınız."

            elif sonuc >= 70:

                belge = "🎉 Teşekkür Belgesi aldınız."

            else:

                belge = "❌ Belge alamadınız."

    return render(
        request,
        "anasayfa.html",
        {
            "sonuc": sonuc,
            "belge": belge,
            "tahmin": tahmin,
        },
    )