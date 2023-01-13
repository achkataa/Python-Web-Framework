from django.contrib import admin

# Register your models here.
from ToDoApp.todo_auth.models import ToDoAppUser


@admin.register(ToDoAppUser)
class ToDoAppUserAdmin(admin.ModelAdmin):
    pass