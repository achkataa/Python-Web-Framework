from django.urls import path

from django_rest.main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]