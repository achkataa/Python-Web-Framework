from django.urls import path

from ToDoApp.web.views import HomeView, DashboardView, SportTodosList, HomeTodosList, WorkTodosList, OtherTodosList, \
    SchoolTodosList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/Sport/', SportTodosList.as_view(), name='Sport'),
    path('dashboard/Home/', HomeTodosList.as_view(), name='Home'),
    path('dashboard/Work/', WorkTodosList.as_view(), name='Work'),
    path('dashboard/Other/', OtherTodosList.as_view(), name='Other'),
    path('dashboard/School/', SchoolTodosList.as_view(), name='School'),

]