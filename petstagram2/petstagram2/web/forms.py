from django import forms

from petstagram2.users.helpers import BootsTrapMixin
from petstagram2.web.models import PetPhoto, Pet


class CreatePhotoForm(forms.ModelForm, BootsTrapMixin):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()


    def save(self, commit=True):
        photo = super().save(commit=False)

        photo.user = self.user
        if commit:
            photo.save()

        return photo

    # tagged_pets = forms.ModelMultipleChoiceField(
    #     queryset=Pet.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )


    class Meta:
        model = PetPhoto
        fields = ('photo','description', 'tagged_pets')

        widgets = {
            'description': forms.Textarea(attrs={'rows':3})
        }



class UpdatePhotoForm(forms.ModelForm, BootsTrapMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')

        widgets = {
            'description': forms.Textarea(attrs={'rows':3})
        }


class DateInput(forms.DateInput):
    input_type = 'date'

class CreatePetForm(forms.ModelForm, BootsTrapMixin):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')

        widgets = {
            'date_of_birth': DateInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.user = user


    def save(self, commit=True):
        pet = super().save(commit=False)

        pet.user = self.user

        if commit:
            pet.save()
        return pet



