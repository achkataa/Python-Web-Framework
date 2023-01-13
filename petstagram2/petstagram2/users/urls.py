from django.urls import path

from petstagram2.users.views import RegisterUserView, LoginUserView, ProfileView, EditProfile

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('prfile/edit/<int:pk>', EditProfile.as_view(), name='edit_profile')
]