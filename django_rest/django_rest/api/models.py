from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(
        max_length=25,
    )

class Product(models.Model):
    name = models.CharField(
        max_length=25,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.01),
        )
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
