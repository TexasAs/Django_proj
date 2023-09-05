from django.urls import path

from orders.views import get_data, add_data, update_data, delete_data

urlpatterns = [
    path('get/', get_data, name='get orders'),
    path('post/', add_data, name='post orders'),
    path('update/<str:pk>', update_data, name='update orders'),
    path('delete/<str:pk>', delete_data, name='delete orders'),
    
]