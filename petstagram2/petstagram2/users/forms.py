from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from petstagram2.users.helpers import BootsTrapMixin
from petstagram2.users.models import PetstagramUserProfile

UserModel = get_user_model()

class CreateUserForm(UserCreationForm, BootsTrapMixin):
    first_name = forms.CharField(
        max_length=PetstagramUserProfile.FIRST_NAME_MAX_LENGTH
    )

    last_name = forms.CharField(
        max_length=PetstagramUserProfile.LAST_NAME_MAX_LENGTH
    )

    profile_picture = forms.URLField()

    gender = forms.ChoiceField(
        choices=PetstagramUserProfile.GENDERS
    )


    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = PetstagramUserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            gender=self.cleaned_data['gender'],
            user=user
        )

        if commit:
            profile.save()
        return user


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()



class LoginForm(AuthenticationForm, BootsTrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class UpdateProfileForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetstagramUserProfile
        exclude = ('user', )


