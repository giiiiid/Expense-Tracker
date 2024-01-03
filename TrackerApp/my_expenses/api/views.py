from django.http import JsonResponse
from rest_framework import response, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from ..models import Expense
from .serializers import ExpenseSerializer
    

class ExpenseCreateList(APIView):
    serializer_class = ExpenseSerializer

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)
        
        serializer = self.serializer_class(expenses, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET","PUT","DELETE"])
def update_delete_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == "GET":
        serializer = ExpenseSerializer(expense)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = ExpenseSerializer(instance=expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        expense.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)