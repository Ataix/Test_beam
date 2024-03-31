from rest_framework import serializers

from .models import Order
from product.serializers import ProductSerializer

from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'items'
        )

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        order.save()
        for item in items:
            item = Product.objects.create(**item)
            order.items.add(item)
        return order
