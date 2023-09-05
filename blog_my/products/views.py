from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serilaizers import ProductSerializer



#def products_page(request):
#    return render(request, 'index.html', {'products': Product.objects.all()})
'''
@api_view(['GET'])
def get_data_product(request):
    items = Product.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_data_product(request):
    serializer = Product(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def update_data_product(request, pk):
    items = Product.objects.all()
    serializer = ProductSerializer(instance=items, data=request.data)
    if serializer.is_valid():
        serializer.save()       
    return Response(serializer.data)   '''

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def get_all_product(request):
    items = Product.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)