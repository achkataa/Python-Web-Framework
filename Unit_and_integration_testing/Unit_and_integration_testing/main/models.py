from django.db import models

# Create your models here.
from Unit_and_integration_testing.main.validators import only_letters_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            only_letters_validator,
        )
    )

    age = models.IntegerField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"