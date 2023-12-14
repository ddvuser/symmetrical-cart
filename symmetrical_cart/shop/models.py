from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager, ProductManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=24, blank=True,null=True)
    surname = models.CharField(max_length=24, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", unique=True, null=False)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):

        return f"Category: \"{self.name}\""

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(default="", unique=True, null=False)
    image = models.ImageField(upload_to='uploads/products/')

    objects = ProductManager()

    def __str__(self):
        return f"Product: \"{self.name}\""

class OrderProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"OrderProduct: \"{self.product.name}\""


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    created_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def get_user_order_products(self, user):
        return self.products.filter(user=user)

    def get_total(self):
        total = 0
        for order_product in self.products.all():
            product_price = order_product.product.price
            total += product_price * order_product.quantity
        return total

    def __str__(self):
        return f"Order: {self.id}"






