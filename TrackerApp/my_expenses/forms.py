from django import forms
from .models import Expense, Book

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
        widgets = {"user":forms.HiddenInput(), "project":forms.HiddenInput()}



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {"user":forms.HiddenInput()}