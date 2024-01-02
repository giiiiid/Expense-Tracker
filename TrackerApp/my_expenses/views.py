from django.shortcuts import render
from .models import Expense
import csv
from django.http import HttpResponse

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
    total_out = str(sum_cash_out).strip("-")

    balance = sum_cash_in + sum_cash_out

    context = {"expenses":expenses, "total_in":sum_cash_in, "total_out":total_out, "balance":balance}
    return render(request, 'index.html', context)


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=expenses.csv"

    writer = csv.writer(response)
    writer.writerow(["Date", "Remark", "Category", "Amount", "Cash Type"])

    expenses = Expense.objects.all()
    for i in expenses:
        writer.writerow([i.date_created, i.remark, i.category, i.amount, i.type_of_expense])
    
    return response