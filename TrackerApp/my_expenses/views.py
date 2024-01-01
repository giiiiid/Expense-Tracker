from django.shortcuts import render
from .models import Expense

# Create your views here.
def homepage(request):
    expenses = Expense.objects.all()
    context = {"expenses":expenses}
    return render(request, 'index.html', contex)


def download_csv(request):
    return "Download csv"