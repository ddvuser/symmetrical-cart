from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Category, Product, Order, OrderProduct

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "category", "release")

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "date_joined")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)
