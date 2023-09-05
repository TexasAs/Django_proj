from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializer



def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})

# GET method
@api_view(['GET'])
def get_data(request):
    items = SalesOrder.objects.all()
    serializer = OrderSerializer(items, many=True)
    return Response(serializer.data)

# POST method
@api_view(['POST'])
def add_data(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# UPDATE method
@api_view(['POST'])
def update_data(request, pk):
    items = SalesOrder.objects.get(id=pk)
    serializer = OrderSerializer(instance=items, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# DELETE method
@api_view(['DELETE'])
def delete_data(request, pk):
    items = SalesOrder.objects.get(id=pk)
    items.delete()
    return Response(f'Sale number {pk} successfully deleted')
