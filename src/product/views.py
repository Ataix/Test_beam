from rest_framework.generics import RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ViewSetMixin

from .models import Product, Shop
from .serializers import ProductSerializer, ShopSerializer


class ProductViewSet(ViewSetMixin,
                     CreateAPIView,
                     RetrieveAPIView,
                     UpdateAPIView,
                     DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopViewSet(ViewSetMixin,
                  CreateAPIView,
                  RetrieveAPIView,
                  UpdateAPIView,
                  DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
