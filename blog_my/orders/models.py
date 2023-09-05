from django.db import models
from django.contrib.auth.models import User

from products.models import Product
from datetime import datetime



class SalesOrder(models.Model):
    
    amount = models.IntegerField()
    date_of_purchase = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    
    

