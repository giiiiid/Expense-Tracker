from django.urls import path
from . import views

urlpatterns = [
    path("create-list-expense", views.ExpenseCreateList.as_view(), name="clexpense"),
    path("edit/<str:id>", views.update_delete_expense, name="edit")
]
