from django.contrib.auth import get_user_model
from django.test import TestCase
from ..forms import RegisterForm, LoginForm

class UserFormsTests(TestCase):

    def test_user_register_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_register_form_invalid(self):
        form_data = {
            'email': 'invalid_email',
            'password1': 'testpassword',
            'password2': 'differentpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_login_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
