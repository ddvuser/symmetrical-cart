from django.test import TestCase
from django.utils import timezone
from ..models import CustomUser, Product, Order, OrderProduct, Category
import datetime

class OrderModelTest(TestCase):
    @classmethod
    def setUp(cls):
        # Set up test data
        cls.user = CustomUser.objects.create(name='testuser', email='test@example.com')
        cls.category = Category.objects.create(name='Test')
        cls.product = Product.objects.create(
            name='Test Product', 
            price=10.0, 
            category=cls.category, 
            description='testing...',
            release=datetime.date(2023,10,10))
        cls.order_product = OrderProduct.objects.create(user=cls.user, product=cls.product)
        cls.order = Order.objects.create(user=cls.user, order_date=timezone.now())
        cls.order.products.add(cls.order_product)

    def test_order_total(self):
        # Test if order total is calculated correctly
        expected_total = self.order_product.quantity * self.product.price
        self.assertEqual(self.order.get_total(), expected_total)

    def test_get_user_order_products(self):
        # Test get_user_order_products method
        user_order_products = self.order.get_user_order_products(self.user)
        self.assertEqual(user_order_products.count(), 1)
        self.assertEqual(user_order_products.first().product, self.product)

    def test_order_string_representation(self):
        # Test string representation of Order model
        expected_repr = f'Order: {self.order.id}'
        self.assertEqual(str(self.order), expected_repr)
