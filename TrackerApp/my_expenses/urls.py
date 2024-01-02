from django.urls import path
from .views import homepage, download_csv, detail_update_expense

urlpatterns = [
    path("", homepage, name="home"),
    path("detail/<str:id>", detail_update_expense, name="detail"),
    path("downloadcsv", download_csv, name="download_csv")
]