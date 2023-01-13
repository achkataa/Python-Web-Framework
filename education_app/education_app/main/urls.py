from django.urls import path

from education_app.main.views import home

urlpatterns = [
    path('', home, name='home')
]