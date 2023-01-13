from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms
from django.views.decorators.cache import cache_page

from django_project.main.forms import DeleteToDoForm
from django_project.main.models import ToDo, Category, Profile

import random

UserModel = get_user_model()

class RegistrationUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()
        return user



class RegistrationUserView(views.CreateView):
    form_class = RegistrationUserForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('todos_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class LogInUser(LoginView):
    template_name = 'login_user.html'

    def get_success_url(self):
        return reverse_lazy('todos_list')

class LogoutUser(LogoutView):
    template_name = 'list_view_todos.html'
    next_page = reverse_lazy('home_view')





class CreateToDo(views.CreateView):
    model = ToDo
    template_name = 'create_to_do.html'
    success_url = reverse_lazy('todos_list')
    fields = '__all__'


class EditToDo(views.UpdateView):
    model = ToDo
    fields = '__all__'
    template_name = 'edit_todo.html'
    success_url = reverse_lazy('todos_list')

class RedirectToHome(views.RedirectView):
    url = reverse_lazy('home_view')


@cache_page(5)
def home_view(request):
    context = {
        'number': random.randint(1, 1024)
    }

    return render(request, 'home.html', context)
# class HomeView(views.TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Hello World'
#         context['number'] = random.randint(1, 1024)
#         return context

class TodosListVIew(LoginRequiredMixin, views.ListView):
    model = ToDo
    template_name = 'list_view_todos.html'

    ordering = ('category__name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(category__name='school')
    #     return queryset

class TodoDetails(views.DetailView):
    model = ToDo
    template_name = 'todo_details.html'
