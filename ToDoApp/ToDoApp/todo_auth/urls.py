from django.urls import path

from ToDoApp.todo_auth.views import RegistrationView, LoginUserView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login_user')
]
