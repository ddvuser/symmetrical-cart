from .models import CustomUser, Order
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'password1', 'password2']

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'autocomplete': 'off',
                                                           'placeholder': 'Email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'autocomplete': 'off',
                                                           'placeholder': 'Name'}))

    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'autocomplete': 'off',
                                                           'placeholder': 'Surname'}))

    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'autocomplete': 'off',
                                                                  'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation', 
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'autocomplete': 'off',
                                                                  'placeholder': 'Password confirmation'}))


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))

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
            'type': 'number'}))

class ConfirmOrderForm(forms.Form):
    receiver_name = forms.CharField(
        max_length=20,
        label='Receiver Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Receiver Name',
            'type': 'text',
        })
    )
    receiver_surname = forms.CharField(
        max_length=20,
        label='Receiver Surname',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Receiver Surname',
            'type': 'text',
        })
    )
    phone = forms.CharField(
        max_length=20,
        label='Phone number',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Phone number',
            'type': 'text',
        })
    )
    address = forms.CharField(
        max_length=200,
        label='Shipping address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'type': 'text',
        })
    )

