from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from ToDoApp.todo_auth.helpers import only_letters_validator
from ToDoApp.todo_auth.managers import PetstagramUserManager


class ToDoAppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 30
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()