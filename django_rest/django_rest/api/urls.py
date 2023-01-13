from django.urls import path

from django_rest.api.views import ProductsListView, CategoriesListVIew

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='prodcts_list'),
    path('categories/', CategoriesListVIew.as_view(), name='categories_list'),
]
