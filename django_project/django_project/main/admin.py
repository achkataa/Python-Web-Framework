from django.contrib import admin

# Register your models here.
from django_project.main.models import ToDo, Category, Users


@admin.register(ToDo)
class AdminToDo(admin.ModelAdmin):
    pass

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(Users)
class AdminUsers(admin.ModelAdmin):
    list_display = ('email',)