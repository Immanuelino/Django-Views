from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    seller = models.CharField(max_length=100, blank=True, null=True)  # Vendedor
    color = models.CharField(max_length=30, blank=True, null=True)  # Color del producto
    product_dimensions = models.CharField(max_length=50, blank=True, null=True)  # Dimensiones del producto
    def __str__(self):
        return self.name