from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from ToDoApp.web.models import TodoCategory, Todo


class HomeView(views.TemplateView):
    template_name = 'home.html'

class DashboardView(LoginRequiredMixin, views.ListView):
    model = TodoCategory
    template_name = 'dashboard.html'
    login_url = reverse_lazy('login_user')




class SportTodosList(LoginRequiredMixin, views.ListView):
    model = Todo
    template_name = 'sport_todos.html'
    login_url = reverse_lazy('login_user')

    def get_queryset(self):
        return super().get_queryset().filter(category_id=4)

class HomeTodosList(LoginRequiredMixin, views.ListView):
    model = Todo
    template_name = 'home_todos.html'
    login_url = reverse_lazy('login_user')

class SchoolTodosList(LoginRequiredMixin, views.ListView):
    model = Todo
    template_name = 'school_todos.html'
    login_url = reverse_lazy('login_user')

class WorkTodosList(LoginRequiredMixin, views.ListView):
    model = Todo
    template_name = 'work_todos.html'
    login_url = reverse_lazy('login_user')

class OtherTodosList(LoginRequiredMixin, views.ListView):
    model = Todo
    template_name = 'other_todos.html'
    login_url = reverse_lazy('login_user')

