import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
    

class Expense(models.Model):

    kinds = (
        ("Cash In", "Cash In"), 
        ("Cash Out", "Cash Out")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField()
    remark = models.CharField(max_length=200, default="")
    project = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    type_of_expense = models.CharField(max_length=100, null=True, choices=kinds)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]


    def __str__(self) -> str:
        return f"{self.type_of_expense} - {self.amount}"