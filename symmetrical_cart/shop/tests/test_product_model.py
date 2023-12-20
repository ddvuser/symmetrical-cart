from django.test import TestCase
from ..models import Product, Category
from django.utils import timezone
from datetime import date

class ProductModelTestCase(TestCase):

    @classmethod
    def setUp(cls):
        category = Category.objects.create(name='Test Category')
        Product.objects.create(
            name='Test Product',
            price=10.50,
            category=category,
            description='Test description',
            slug='test-product',
            image='path/to/image.png',
            release=timezone.now().date()
        )

    def test_product_creation(self):
        # Test if a product is created correctly
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.price, 10.50)
        self.assertEqual(product.category.name, 'Test Category')
        self.assertEqual(product.description, 'Test description')
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(product.image, 'path/to/image.png')
        self.assertTrue(isinstance(product.release, date))

    def test_product_str_representation(self):
        # Test the string representation of the Product model
        product = Product.objects.get(name='Test Product')
        self.assertEqual(str(product), "Product: \"Test Product\"")
