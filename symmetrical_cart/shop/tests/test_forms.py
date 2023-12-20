from django.contrib.auth import get_user_model
from django.test import TestCase
from ..forms import RegisterForm, LoginForm, ProductQuantityForm, ConfirmOrderForm

class UserFormsTests(TestCase):

    def test_user_register_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'name': 'John',
            'surname': 'Doe',
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

class TestProductQuantityForm(TestCase):
    def test_valid_product_quantity_form(self):
        form_data = {'quantity': '5'}
        form = ProductQuantityForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_product_quantity_form(self):
        form_data = {'quantity': '-1'}
        form = ProductQuantityForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestConfirmOrderForm(TestCase):
    def test_valid_confirm_order_form(self):
        form_data = {
            'receiver_name': 'John',
            'receiver_surname': 'Doe',
            'phone': '1234567890',
            'address': '123 Test St, Test City'
        }
        form = ConfirmOrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_confirm_order_form(self):
        # Test when required fields are left empty
        form_data = {
            'receiver_name': '',
            'receiver_surname': '',
            'phone': '',
            'address': ''
        }
        form = ConfirmOrderForm(data=form_data)
        self.assertFalse(form.is_valid())
