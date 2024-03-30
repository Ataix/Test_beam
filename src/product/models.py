from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    product_shop = models.OneToOneField(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
