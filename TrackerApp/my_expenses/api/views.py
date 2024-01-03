from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import response, status
from rest_framework.views import APIView
from ..models import Expense
from .serializers import ExpenseSerializer

    

class ExpenseList(APIView):
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
        