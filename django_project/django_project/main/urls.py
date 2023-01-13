from django.urls import path

from django_project.main.views import home_view, TodosListVIew, TodoDetails, CreateToDo, EditToDo, RegistrationUserView, \
    LogInUser, LogoutUser

urlpatterns = [
    path('', home_view, name='home_view'),
    path('todo/list/', TodosListVIew.as_view(), name='todos_list'),
    path('todo/details/<int:pk>', TodoDetails.as_view(), name='todo_details'),
    path('create/todo/', CreateToDo.as_view(), name='create_todo'),
    path('edit/todo/<int:pk>/', EditToDo.as_view(), name='edit_todo'),
    path('register/user/', RegistrationUserView.as_view(), name='register_user'),
    path('login/user/', LogInUser.as_view(), name='login_user'),
    path('logout/user/', LogoutUser.as_view(), name='logout_user'),
]