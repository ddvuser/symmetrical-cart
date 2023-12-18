import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    release_year = django_filters.NumberFilter(field_name='release__year', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['price__lt', 'price__gt', 'release_year', 'name', 'category']
