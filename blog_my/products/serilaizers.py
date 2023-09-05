from rest_framework.serializers import ModelSerializer

from products.models import Product


        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'description_category', 'receipt_date']
        #fields = '__all__'
