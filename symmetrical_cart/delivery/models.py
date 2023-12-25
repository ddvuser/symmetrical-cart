from django.db import models
from shop.models import Order

class Employee(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)
    delivery_location = models.CharField(max_length=100, blank=True, null=True)

    current_orders = models.ManyToManyField(Order, related_name='current_delivery_user', blank=True)

    delivered_orders = models.ManyToManyField(Order, related_name='delivered_delivery_user', blank=True)

    def __str__(self):
        return f"DeliveryMan: {self.name} {self.surname}"

    class Meta:
        verbose_name = 'Delivery User'
        verbose_name_plural = 'Delivery Users'
