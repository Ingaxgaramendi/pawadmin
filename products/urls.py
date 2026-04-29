from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    CategoryViewSet,
    BrandViewSet,
    PetTypeViewSet
)

router = DefaultRouter()

router.register(
    r'products',
    ProductViewSet
)

router.register(
    r'categories',
    CategoryViewSet
)

router.register(
    r'brands',
    BrandViewSet
)

router.register(
    r'pet-types',
    PetTypeViewSet
)

urlpatterns = router.urls

from django.urls import path
from .views import product_list

urlpatterns = [
    path('productos/', product_list, name='product_list'),
]