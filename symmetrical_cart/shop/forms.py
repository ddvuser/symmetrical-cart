from .models import CustomUser, Order
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.validators import MinValueValidator
from .validators.form_fields import (
    phone_validator,
    name_validator,
    address_validator,
    quantity_validator,
    password_validator)


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'password1', 'password2']

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'autocomplete': 'off',
                   'placeholder': 'Email',
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'autocomplete': 'off',
                   'placeholder': 'Name'
            }
        ),
        validators=[name_validator]

    )
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'autocomplete': 'off',
                   'placeholder': 'Surname'
            }
        ),
        validators=[name_validator]
    )
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'autocomplete': 'off',
                   'placeholder': 'Password'
            }
        ),
        validators=[password_validator]
    )
    password2 = forms.CharField(
        label='Password confirmation', 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'autocomplete': 'off',
                   'placeholder': 'Password confirmation'
            }
        ),
        validators=[password_validator]
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Email',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password',
            }
        )
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'Old Password'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'New Password'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'Confirm New Password'
        })

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class CustomPasswordResetConfirmForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )

class ProductQuantityForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Quantity',
            'type': 'number',
            'id': 'quantity-input',
        }),
        validators=[MinValueValidator(1), quantity_validator]
        
    )

class ConfirmOrderForm(forms.Form):
    receiver_name = forms.CharField(
        max_length=20,
        label='Receiver Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Receiver Name',
            'type': 'text',
        }),
        validators=[name_validator]
    )
    receiver_surname = forms.CharField(
        max_length=20,
        label='Receiver Surname',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Receiver Surname',
            'type': 'text',
        }),
        validators=[name_validator]
    )
    phone = forms.CharField(
        max_length=20,
        label='Phone number',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Phone number',
            'type': 'text',
        }),
        validators=[phone_validator]
    )
    address = forms.CharField(
        max_length=200,
        label='Shipping address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'type': 'text',
        }),
        validators=[address_validator]
    )

class EditUserForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'type': 'text',
            'id': 'name-input',
            'name': 'name-input',

        }),
        validators=[name_validator]
    )
    surname = forms.CharField(
        max_length=20,
        label='Surname',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Surname',
            'type': 'text',
            'id': 'surname-input',
            'name': 'surname-input',
            
        }),
        validators=[name_validator]
    )
    phone = forms.CharField(
        max_length=20,
        label='Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
            'type': 'text',
            'id': 'phone-input',
            'name': 'phone-input',
            
        }),
        validators=[phone_validator]
    )
    address = forms.CharField(
        max_length=200,
        label='Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'type': 'text',
            'id': 'address-input',
            'name': 'address-input',
        }),
        validators=[address_validator]
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = False
        self.fields['address'].required = False

