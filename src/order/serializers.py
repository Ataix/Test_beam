from rest_framework import serializers

from .models import Order
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'items'
        )
