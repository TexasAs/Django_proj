from django.db import models
from PIL import Image


class Product(models.Model):
    
    PRODUCT_CATEGORY = [
        ('technice', 'th'),
        ('book', 'bk'),
        ('phone', 'ph'),
        ('food', 'fd'),
        ('cloth', 'cl'),
        ('other', 'ot'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='None')
    description_category = models.CharField(max_length=15, choices=PRODUCT_CATEGORY, default='other')
    product_photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default='-')
    receipt_date = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.name
    
