import django_filters
from shop.models import Order 

class OrderFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Order 
        fields = ['status']
