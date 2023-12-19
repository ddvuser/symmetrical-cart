from django.test import TestCase
from ..models import Category

class CategoryModelTest(TestCase):
    @classmethod
    def setUp(cls):
        # Create test data that will be used by the tests
        Category.objects.create(name='Category 1', slug='category-1')
        Category.objects.create(name='Category 2', slug='category-2')

    def test_get_all_categories(self):
        # Test the get_all_categories method
        categories = Category.get_all_categories()
        self.assertEqual(categories.count(), 2)  # Make sure two categories are created

    def test_category_str_representation(self):
        # Test the string representation of a category
        category = Category.objects.get(name='Category 1')
        self.assertEqual(str(category), 'Category: "Category 1"')

    def test_unique_slug(self):
        # Test uniqueness of slug field
        with self.assertRaises(Exception):
            # Attempt to create a category with a duplicate slug
            Category.objects.create(name='Duplicate Category', slug='category-1')
