from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, OrderProduct, Order, Category
from .forms import ProductQuantityForm, ConfirmOrderForm
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    products = Product.objects.get_all_products().order_by('name')
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

def category(request):
    categories = Category.objects.all()
    context = {
        "categories": categories 
    }
    return render(request, 'category/category.html', context)

def category_detail(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 8)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'category/category_detail.html', context)

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
        order_products = order.get_user_order_products(request.user).order_by("order")
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
    initial = {
        'receiver_name': request.user.name,
        'receiver_surname': request.user.surname,
        'phone': request.user.phone,
        'address': request.user.address,

    }
    form = ConfirmOrderForm(initial)
    context = {
        'order': order,
        'order_products': order_products,
        'form': form,
    }
    return render(request, 'cart/checkout.html', context)

@login_required()
def confirm_order(request):
    if request.method == "POST":
        form = ConfirmOrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.filter(user=request.user, ordered=False).first()
            cleaned_data = form.cleaned_data

            order.receiver_name = cleaned_data.get('receiver_name')
            order.receiver_surname = cleaned_data.get('receiver_surname')
            order.phone = cleaned_data.get('phone')
            order.address = cleaned_data.get('address')

            order.ordered = True
            order.save()
        
            # Send email confirmation
            subject = 'Order Confirmation'
            email = request.user.email
            message = f'We\' received your order.'
            
            send_mail(subject, message, 'symmetrical_cart@example.com', [email], fail_silently=False)
            return redirect('cart')

