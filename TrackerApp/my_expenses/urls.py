from django.urls import path
from .views import homepage, download_csv

urlpatterns = [
    path("", homepage, name="home"),
    path("downloadcsv", download_csv, name="download_csv")
]