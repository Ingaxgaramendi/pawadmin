from django.db import models

from products.models import Product


class StockMovement(models.Model):

    # NUEVO
    ENTRY = 'ENTRY'
    EXIT = 'EXIT'

    MOVEMENT_TYPES = [
        (ENTRY,'Entry'),
        (EXIT,'Exit'),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='movements'
    )

    quantity = models.PositiveIntegerField()

    movement_type = models.CharField(
        max_length=20,
        choices=MOVEMENT_TYPES
    )

    notes = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.product.name} {self.movement_type}"