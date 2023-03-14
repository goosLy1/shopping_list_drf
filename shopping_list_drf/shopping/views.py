from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import Shopping
from .serializers import ShoppingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class ShoppingAPIList(generics.ListCreateAPIView):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer

# class ShoppingApiView(APIView):
#     def get(self, request):
#         lst = Shopping.objects.all()
#         print(ShoppingSerializer(lst, many = True).data)
#         print(request.user)
#         return Response({'shopping_lists': ShoppingSerializer(lst, many = True).data})
    
#     def post(self, request):
#         serializer = ShoppingSerializer(data = request.data, context = {'user_id': request.user.id})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'shopping_list': serializer.data})


# class ShoppingApiView(generics.ListAPIView):
#     queryset = Shopping.objects.all()
#     serializer_class = ShoppingSerializer
