from django.contrib import admin

# Register your models here.
from ToDoApp.web.models import TodoCategory, Todo


@admin.register(TodoCategory)
class TodoCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
