from django.urls import path
from .views import homepage, download_csv, detail_update_expense, delete_expense

urlpatterns = [
    path("", homepage, name="home"),
    path("detail/<str:id>", detail_update_expense, name="detail"),
    path("delete/<str:id>", delete_expense, name="delete"),
    path("downloadcsv", download_csv, name="download_csv")
]