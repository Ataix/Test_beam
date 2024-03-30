from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.user}"s order {self.created_at}'
