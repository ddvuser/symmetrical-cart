from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'autocomplete': 'off',
                                                           'placeholder': 'Email'}))
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
