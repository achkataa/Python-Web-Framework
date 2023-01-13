from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Value should contain only letters')


class BootsTrapMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'