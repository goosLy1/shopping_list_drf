from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import Shopping
from .serializers import ShoppingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ShoppingApiView(APIView):
    def get(self, request):
        lst = Shopping.objects.all().values()

        return Response({'shopping_lists': list(lst)})
    
    def post(self, request):
        new_list = Shopping.objects.create(
            label = request.data['label'],
            user_id = request.data['user_id']
        )
        return Response({'shopping_list': model_to_dict(new_list)})


# class ShoppingApiView(generics.ListAPIView):
#     queryset = Shopping.objects.all()
#     serializer_class = ShoppingSerializer
