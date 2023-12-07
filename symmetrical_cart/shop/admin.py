from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Category, Product

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Product)
