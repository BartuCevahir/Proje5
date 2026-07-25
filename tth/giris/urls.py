from django.urls import path
from .views import giris

urlpatterns = [
    path("", giris, name="giris"),
]