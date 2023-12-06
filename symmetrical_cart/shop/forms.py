from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm


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
