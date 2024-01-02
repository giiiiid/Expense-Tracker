from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Expense
from .forms import ExpenseForm
import csv
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    user = request.user
    expenses = Expense.objects.filter(user=user)

    cash_in = []
    cash_out = []

    for i in expenses:
        if i.type_of_expense == "Cash In":
           cash_in.append(i.amount)
        elif i.type_of_expense == "Cash Out":
            cash_out.append(i.amount)

    sum_cash_in = sum([i for i in cash_in])
    sum_cash_out = sum([i for i in cash_out])
    total_out = str(sum_cash_out).strip("-")

    balance = -(sum_cash_out) + sum_cash_in

    forms = ExpenseForm(initial={"user":user})
    instance_model = user
    if request.method == "POST":
        forms = ExpenseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("home")
    
    context = {
            "expenses":expenses, "total_in":sum_cash_in, "total_out":total_out, 
            "balance":balance, "forms":forms
            }
    return render(request, "index.html", context)



def detail_update_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == "POST":
        forms = ExpenseForm(request.POST, instance=expense)
        if forms.is_valid():
            forms.save()
            return redirect("detail", expense.id)
        
    else:
        forms = ExpenseForm(instance=expense)
        
    context = {"expense":expense, "forms":forms}
    return render(request, "detail.html", context)




def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=expenses.csv"

    writer = csv.writer(response)
    writer.writerow(["Date", "Remark", "Category", "Amount", "Cash Type"])

    user = request.user
    expenses = Expense.objects.filter(user=user)
    for i in expenses:
        writer.writerow([i.date_created, i.remark, i.category, i.amount, i.type_of_expense])
    
    return response