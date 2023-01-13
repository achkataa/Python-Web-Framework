from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram2.users.managers import PetstagramUserManager
from petstagram2.users.validators import only_letters_validator


class PetstagramUserModel(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 40

    username = models.CharField(
        unique=True,
        max_length=USERNAME_MAX_LENGTH
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()

    def __str__(self):
        return f"{self.username}"

class PetstagramUserProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    GENDERS_MAX_LENGTH = 7

    MALE = 'Male'
    FEMALE = 'Female'

    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator
        )
    )

    profile_picture = models.URLField()

    gender = models.CharField(
        max_length=GENDERS_MAX_LENGTH,
        choices=GENDERS,
        null=True,
        blank=True,

    )

    user = models.OneToOneField(
        PetstagramUserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.user} profile"

