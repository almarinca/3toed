from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name="Product Name")
    description = models.TextField(max_length=300, verbose_name="Product Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Product Price"
    )
    available = models.BooleanField(default=True, verbose_name="Product Available")
    image = models.ImageField(
        upload_to="media", null=True, blank=True, verbose_name="Product image"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Product Creation Date")

    def __str__(self):
        return self.name
