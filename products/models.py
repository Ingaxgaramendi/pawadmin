from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class PetType(models.Model):
    name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=150
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )

    pet_types = models.ManyToManyField(
        PetType
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name