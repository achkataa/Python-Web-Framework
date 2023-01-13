from django.urls import path

from petstagram2.web.views import HomeView, DashboardView, AddPetView, AddPhotoView, PhotoDetailView, EditPetPhoto, \
    DeletePetPhoto

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('pet/create/', AddPetView.as_view(), name='create_pet'),
    path('photo/create', AddPhotoView.as_view(), name='create_photo'),
    path('photo/details/<int:pk>/', PhotoDetailView.as_view(), name='photo_details'),
    path('photo/edit/<int:pk>', EditPetPhoto.as_view(), name='photo_edit'),
    path('photo/delete/<int:pk>', DeletePetPhoto.as_view(), name='photo_delete')

]