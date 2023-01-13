from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram2.web.forms import CreatePhotoForm, UpdatePhotoForm, CreatePetForm
from petstagram2.web.models import PetPhoto, Pet


class HomeView(views.TemplateView):
    template_name = 'web_templates/home_page.html'

class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'web_templates/dashboard.html'
    context_object_name = 'pets_photos'


class AddPetView(views.CreateView):
    template_name = 'web_templates/pet_create.html'
    model = Pet
    form_class = CreatePetForm

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('profile', kwargs={'pk':pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class AddPhotoView(views.CreateView):
    template_name = 'web_templates/photo_create.html'
    model = PetPhoto
    form_class = CreatePhotoForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class PhotoDetailView(views.DetailView):
    template_name = 'web_templates/photo_details.html'
    model = PetPhoto
    context_object_name = 'petphoto'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

class EditPetPhoto(views.UpdateView):
    template_name = 'web_templates/photo_edit.html'
    model = PetPhoto
    form_class = UpdatePhotoForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('photo_details', kwargs={'pk':pk})

class DeletePetPhoto(views.DeleteView):
    model = PetPhoto
    template_name = 'web_templates/photo_delete.html'
    success_url = reverse_lazy('dashboard')
