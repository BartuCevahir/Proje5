from django.urls import path
from .views import anasayfa

urlpatterns = [
    path("", anasayfa, name="yks"),
]