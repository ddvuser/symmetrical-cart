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

address_regex = r'^[a-zA-Z0-9\s,\'-]*$'

address_validator = RegexValidator(
    regex=address_regex,
    message='Enter a valid shipping address.',
    code='invalid_address'
)

quantity_regex = r'^\d+$'

quantity_validator = RegexValidator(
    regex=quantity_regex,
    message='Product quantity must be a positive integer.',
    code='invalid_quantity'
)

password_regex =  r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-_]).{8,}$'
password_validator = RegexValidator(
    regex=password_regex,
    message='''
                Minimum eight characters, 
                at least one upper case English letter, 
                one lower case English letter, 
                one number and one special character
            ''',
    code = 'invalid_password'
)
