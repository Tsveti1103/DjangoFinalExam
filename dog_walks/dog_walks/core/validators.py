import regex as re
from django.core.exceptions import ValidationError
from django.core import validators

validators.validate_email.message = 'Моля въведете валиден имеил!'


def only_letters_validator(value, message):
    for symbol in value:
        if not symbol.isalpha():
            raise ValidationError(message)


def only_cyrillic_letters_validator(value):
    pattern = "[\p{Cyrillic}* ]*"
    cyrillic_letters = re.match(pattern, value)
    if value != cyrillic_letters[0]:
        raise ValidationError('Моля използвайте само български букви')


class OptionalSchemeURLValidator(validators.URLValidator):
    def __call__(self, value):
        if '://' not in value:
            value = 'http://' + value
        super(OptionalSchemeURLValidator, self).__call__(value)
