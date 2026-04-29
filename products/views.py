from rest_framework import viewsets
from django.shortcuts import render

from .models import (
    Product,
    Category,
    Brand,
    PetType
)

from .serializers import (
    ProductSerializer,
    CategorySerializer,
    BrandSerializer,
    PetTypeSerializer
)


class ProductViewSet(
    viewsets.ModelViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(
    viewsets.ModelViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(
    viewsets.ModelViewSet
):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class PetTypeViewSet(
    viewsets.ModelViewSet
):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer
    

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})