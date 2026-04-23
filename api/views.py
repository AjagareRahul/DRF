from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products, Product
from .serializers import ProductSerializer, ProductsSerializer

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request, 'api/home.html', {'products': products})


@api_view(['GET'])
def get_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    serializer = ProductsSerializer(product, many=True)
    return Response(serializer.data)
