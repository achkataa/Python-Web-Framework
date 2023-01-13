from django.contrib import admin

# Register your models here.
from petstagram2.users.models import PetstagramUserModel, PetstagramUserProfile


@admin.register(PetstagramUserModel)
class PetstagramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(PetstagramUserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass