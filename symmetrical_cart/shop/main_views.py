from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.get_all_products()
    paginator = Paginator(products, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, "index.html", context=context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {'product': product})
