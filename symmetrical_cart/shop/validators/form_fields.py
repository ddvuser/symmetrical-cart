from django.core.validators import RegexValidator

phone_regex =  r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

phone_validator = RegexValidator(
    regex=phone_regex,
    message='Enter a valid phone number.',
    code='invalid_phone_number'
)

name_regex = r'^[A-Z][a-zA-Z]{3,}(?: [A-Z][a-zA-Z]*){0,2}$'

name_validator = RegexValidator(
    regex = name_regex,
    message = 'Enter a valid name/surname',
    code = 'invalid_name'
)
