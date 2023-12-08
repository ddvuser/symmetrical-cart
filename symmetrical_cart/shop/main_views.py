from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

def index(request):
    context = {
        'products': Product.objects.get_all_products()
    }
    return render(request, "index.html", context=context)
