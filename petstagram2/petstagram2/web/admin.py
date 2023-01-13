from django.contrib import admin

# Register your models here.
from petstagram2.web.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass