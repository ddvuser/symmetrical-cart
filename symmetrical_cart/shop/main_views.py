from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, OrderProduct, Order
from .forms import ProductQuantityForm, ConfirmOrderForm
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    products = Product.objects.get_all_products()
    paginator = Paginator(products, 8)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, "index.html", context=context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {'product': product})

@login_required()
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    order_product, created = OrderProduct.objects.get_or_create(user=request.user, 
                                                 ordered=False,
                                                product=product)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # Add new product or update quantity to existing order
    if order_qs.exists():
        order = order_qs[0]
        # Check for the product
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            msg = f"Product: {product.name} quantity is updated."
            messages.info(request, msg)
            return redirect('cart')
        else:
            order.products.add(order_product)
            msg = f"Product: {product.name} is added to your cart."
            return redirect('cart')
    # Create new order and add new product
    else:
        order = Order.objects.create(user=request.user,
                                     order_date=timezone.now())
        order.products.add(order_product)
        msg = f"Product: {product.name} is added to your cart."
        return redirect('cart')

@login_required()
def update_product_quantity(request, product_slug):
    new_quantity = request.POST.get('quantity')
    if request.method == "POST":
        if not new_quantity.isnumeric():
            msg = f"Product quantity can only be numeric."
            messages.info(request, msg)
            return redirect('cart')

        if int(new_quantity) < 1:
            msg = f"Product quantity cannot be less than 1."
            messages.info(request, msg)
            return redirect('cart')
        else:
            product = get_object_or_404(Product, slug=product_slug)
            order_product = OrderProduct.objects.get(user=request.user,
                                                     ordered=False,
                                                     product=product)
            order_product.quantity = request.POST.get('quantity')
            order_product.save()
            msg = f"Product: {product.name} quantity is updated."
            messages.info(request, msg)
            return redirect('cart')

@login_required()
def cart(request):
    # Fetch the order for the logged-in user
    order = Order.objects.filter(user=request.user, ordered=False).first()
    form = ProductQuantityForm()
    order_products = []
    page_obj = {}
    context = {}
    if order:
        order_products = order.get_user_order_products(request.user)
        paginator = Paginator(order_products, 7)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "form": form,
            "order_products": page_obj,
        }

    return render(request, 'cart/cart.html', context)

@login_required()
def remove_from_cart(request, orderproduct_id):
    order_product = get_object_or_404(OrderProduct, id=orderproduct_id)
    order_product.delete()
    return redirect('cart')

@login_required()
def checkout(request):
    order = Order.objects.filter(user=request.user, ordered=False).first()
    order_products = order.get_user_order_products(request.user)
    form = ConfirmOrderForm()
    context = {
        'order': order,
        'order_products': order_products,
        'form': form,
    }
    return render(request, 'cart/checkout.html', context)

@login_required()
def confirm_order(request):
    if request.method == "POST":
        address = request.POST.get('address')
        order = Order.objects.filter(user=request.user, ordered=False).first()
        order.address = address
        order.ordered = True
        order.save()
        return redirect('cart')

