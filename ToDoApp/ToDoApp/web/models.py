from django.db import models

# Create your models here.


class TodoCategory(models.Model):
    NAME_MAX_LENGTH=20
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    def __str__(self):
        return f"{self.name}"



class Todo(models.Model):
    NAME_MAX_LENGTH=30
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    is_done = models.BooleanField(
        default=False
    )

    category = models.ForeignKey(
        TodoCategory,
        on_delete=models.CASCADE
    )


