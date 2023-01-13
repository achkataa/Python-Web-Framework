import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from petstagram2.users.models import PetstagramUserModel

UserModel = get_user_model()

class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 7

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (BUNNY, 'Buuny'),
        (PARROT, 'Parrot'),
        (FISH, 'Fish'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(
        max_length=PET_NAME_MAX_LENGTH
    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPES
    )

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    @property
    def pet_age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return f"{self.name}"





class PetPhoto(models.Model):
    PHOTO_LIKES_MIN_VALUE = 0

    photo = models.ImageField()

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
        validators=(
            MinValueValidator(PHOTO_LIKES_MIN_VALUE),
        )
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )




