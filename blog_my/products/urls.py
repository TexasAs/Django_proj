from django.urls import path
from products.views import snippet_detail, get_all_product, add_product


'''
from products.views import get_data_product, add_data_product, update_data_product

urlpatterns = [
    path('get/', get_data_product, name='get product'),
    path('post/', add_data_product, name='post product'),
    path('update/<str:pk>/', update_data_product, name='update product'),
]
'''

urlpatterns = [
    path('get/<str:pk>', snippet_detail, name='get update and delete product'),
    path('get_all/', get_all_product, name='get all product'),
    path('post/', add_product, name='add product'),
]