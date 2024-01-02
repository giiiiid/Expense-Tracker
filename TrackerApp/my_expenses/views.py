from django.shortcuts import render, redirect
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
        if i.type_of_expense == "Cash Out":
           cash_out.append(i.amount)
        elif i.type_of_expense == "Cash In":
            cash_in.append(i.amount)

    sum_cash_in = sum([i for i in cash_in])
    sum_cash_out = sum([i for i in cash_out])
    total_out = str(sum_cash_out).strip("-")

    balance = sum_cash_in + sum_cash_out
    # val = float()
    forms = ExpenseForm(initial={"user":user})
    instance_model = user
    if request.method == "POST":
        forms = ExpenseForm(request.POST)
        if forms.is_valid():
            forms.save()

            val = 0
            amt_value = forms.cleaned_data["amount"]
            val += amt_value
            print(type(amt_value))
            print(val)
            
            return redirect("home")
    
    net_bal_calc = [i.amount for i in expenses]
    # if amt_value in net_bal_calc:
    #     net_bal_calc.remove(amt_value)
    #     val += amt_value
    net_bal = net_bal_calc[0] + sum([i for i in net_bal_calc][1::])
    print(net_bal_calc)
    # print(val)

    print(expenses)
    context = {
            "expenses":expenses, "total_in":sum_cash_in, "total_out":total_out, 
            "balance":balance, "forms":forms, "net_bal":net_bal
            }
    return render(request, "index.html", context)


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=expenses.csv"

    writer = csv.writer(response)
    writer.writerow(["Date", "Remark", "Category", "Amount", "Cash In", "Cash Out"])

    user = request.user
    expenses = Expense.objects.filter(user=user)
    for i in expenses:
        writer.writerow([i.date_created, i.remark, i.category, i.amount, i.type_of_expense])
    
    return response