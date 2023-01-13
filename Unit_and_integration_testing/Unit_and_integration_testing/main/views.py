from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from Unit_and_integration_testing.main.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile_create.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})

class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user.username
        else:
            context['user'] = 'No user'

        return context


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile_details.html'