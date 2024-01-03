from django.urls import path, include
from .views import homepage, download_csv, detail_update_expense, delete_expense

urlpatterns = [
    path("", homepage, name="home"),
    path("detail/<str:id>", detail_update_expense, name="detail"),
    path("delete/<str:id>", delete_expense, name="delete"),
    path("downloadcsv", download_csv, name="download_csv"),
    path("api/v1/", include("my_expenses.api.urls"))
]