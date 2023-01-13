from django.core.exceptions import ValidationError


def only_letters_validator(value):
    VALIDATION_ERROR_MESSAGE = 'This value should contain only letters'
    for char in value:
        if not char.isalpha():
            return ValidationError(VALIDATION_ERROR_MESSAGE)
