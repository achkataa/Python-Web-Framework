from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError('value should contain only latters')