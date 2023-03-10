from django.shortcuts import render
from rest_framework import generics
from .models import Shopping
from .serializers import ShoppingSerializer

class ShoppingApiView(generics.ListAPIView):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer
