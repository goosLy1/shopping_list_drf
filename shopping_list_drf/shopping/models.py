from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    label = models.CharField(max_length=50)
    price = models.FloatField()
    

    def __str__(self) -> str:
        return self.label
    
class Shopping(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    label = models.CharField(max_length=120)
    products = models.ManyToManyField(Product)
    

    def __str__(self) -> str:
        return self.label
