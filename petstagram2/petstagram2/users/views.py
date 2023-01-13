from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from django.views import generic as views

from petstagram2.users.forms import CreateUserForm, LoginForm, UpdateProfileForm
from petstagram2.users.models import PetstagramUserModel, PetstagramUserProfile
from petstagram2.web.models import Pet, PetPhoto


class RegisterUserView(views.CreateView):
    template_name = 'accounts_templates/profile_create.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class LoginUserView(LoginView):
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('dashboard')
    template_name = 'accounts_templates/login.html'


class ProfileView(views.DetailView):
    template_name = 'accounts_templates/profile_details.html'
    model = PetstagramUserProfile
    context_object_name = 'profile_info'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        pets = Pet.objects.filter(user_id=self.request.user.pk)
        photos = PetPhoto.objects.filter(user_id=self.request.user.pk)
        pet_photos_count = len(photos)
        pet_photo_likes = sum([photo.likes for photo in photos])

        context_data.update({
            'pets': pets,
            'photos_count': pet_photos_count,
            'photo_likes': pet_photo_likes
        })

        return context_data

class EditProfile(views.UpdateView):
    template_name = 'accounts_templates/profile_edit.html'
    model = PetstagramUserProfile
    form_class = UpdateProfileForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk':pk})