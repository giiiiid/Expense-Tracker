from django.urls import path
from . import views

urlpatterns = [
    path("create-list-expense", views.expense_list_create, name="create_list_expense"),
    path("clexpense", views.ExpenseList.as_view(), name="clexpense")
]
