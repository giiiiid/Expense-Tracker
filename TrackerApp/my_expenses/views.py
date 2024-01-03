from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Expense, Book
from .forms import ExpenseForm
import csv


# Create your views here.
def books(request):
    books = Book.objects.all()

    context = {"books":books}
    return render(request, "base.html", context)

def project_expenses(request, name):
    user = request.user
    book = Book.objects.get(name=name)
    expenses = book.expense_set.all()

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
            return redirect("book_expense", book.name)
    
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
            return redirect("book_expense", expense.project.name)
        
    else:
        forms = ExpenseForm(instance=expense)
        
    context = {"expense":expense, "forms":forms}
    return render(request, "detail.html", context)



def delete_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == "POST":
        expense.delete()
        return redirect("book_expense", expense.project.name)
    return render(request, "delete.html")




def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=expenses.csv"

    writer = csv.writer(response)
    writer.writerow(["Date", "Remark", "Category", "Amount", "Cash Type"])

    user = request.user
    expenses = Expense.objects.filter(user=user)
    for i in expenses:
        if i.type_of_expense == "Cash In":
            i.amount = i.amount

        elif i.type_of_expense == "Cash Out":
            i.amount = -i.amount
        writer.writerow([i.date_created, i.remark, i.category, i.amount, i.type_of_expense])

    return response