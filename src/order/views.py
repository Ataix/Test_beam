from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ViewSetMixin

from .models import Order


class OrderViewSet(ViewSetMixin,
                   CreateAPIView,
                   RetrieveAPIView,
                   UpdateAPIView,
                   DestroyAPIView):
    queryset = Order.objects.all()

