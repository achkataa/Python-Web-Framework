from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from django_project.main.manager import UsersManager


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = UsersManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30
    )

    user = models.OneToOneField(
        Users,
        on_delete=models.CASCADE
    )





class Category(models.Model):
    name = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(
        max_length=30
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

