from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from ToDoApp.todo_auth.forms import RegistrationForm, LoginUserForm


class RegistrationView(views.CreateView):
    template_name = 'auth/profile_create.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class LoginUserView(LoginView):
    template_name = 'auth/login_page.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('dashboard')



