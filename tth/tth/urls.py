from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("giris.urls")),
    path("hesapla/", include("anasayfa.urls")),
    path("yks/", include("yks.urls")),
    path("admin/", admin.site.urls),
    path("anasayfa/", include("anasayfa.urls")),
]