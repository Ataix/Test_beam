from rest_framework.generics import RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ViewSetMixin

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(ViewSetMixin,
                   CreateAPIView,
                   RetrieveAPIView,
                   UpdateAPIView,
                   DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
