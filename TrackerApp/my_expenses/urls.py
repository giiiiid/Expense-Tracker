from django.urls import path, include
from .views import books, project_expenses, download_csv, detail_update_expense, delete_expense

urlpatterns = [
    path("home", books, name="books"),
    path("book-expenses/<str:name>", project_expenses, name="book_expense"),
    path("detail/<str:id>", detail_update_expense, name="detail"),
    path("delete/<str:id>", delete_expense, name="delete"),
    path("downloadcsv/<str:name>", download_csv, name="download_csv"),
    path("api/v1/", include("my_expenses.api.urls"))
]