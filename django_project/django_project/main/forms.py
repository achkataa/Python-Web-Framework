from django import forms

from django_project.main.helpers import DisableFields
from django_project.main.models import ToDo


class DeleteToDoForm(forms.ModelForm, DisableFields):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disable_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = ToDo
        fields = '__all__'

