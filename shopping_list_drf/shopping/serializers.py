from rest_framework import serializers
from .models import Shopping






# class ShoppingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shopping
#         fields = ('label', 'products')


class ProductSerializer(serializers.Serializer):
    label = serializers.CharField(max_length = 255)
    price = serializers.FloatField()



class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = ("user", "label", "products")