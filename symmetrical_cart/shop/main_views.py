from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import get_object_or_404

def index(request):
    context = {
        'products': Product.objects.get_all_products()
    }
    return render(request, "index.html", context=context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {'product': product})
