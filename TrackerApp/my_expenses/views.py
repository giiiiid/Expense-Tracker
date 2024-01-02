from django.shortcuts import render
from .models import Expense

# Create your views here.
def homepage(request):
    expenses = Expense.objects.all()

    cash_in = []
    cash_out = []

    for i in expenses:
        if i.type_of_expense == "Cash Out":
           cash_out.append(i.amount)
        elif i.type_of_expense == "Cash In":
            cash_in.append(i.amount)

    sum_cash_in = sum([i for i in cash_in])
    sum_cash_out = sum([i for i in cash_out])
    
    total = sum_cash_in + sum_cash_out

    context = {"expenses":expenses, "total_in":sum_cash_in, "total_out":sum_cash_out, "total":total}
    return render(request, 'index.html', context)


def download_csv(request):
    return "Download csv"