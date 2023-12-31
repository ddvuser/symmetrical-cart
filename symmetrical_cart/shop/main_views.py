from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, OrderProduct, Order, Category
from delivery.models import Employee
from .forms import ProductQuantityForm, ConfirmOrderForm, RateDeliveryForm
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Avg

def index(request):
    product_filter = ProductFilter(request.GET, Product.objects.get_all_products().order_by("name"))
    filtered_products = product_filter.qs
    paginator = Paginator(filtered_products, 8)
    categories = Category.objects.all()

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "product_filter": product_filter,
        "categories": categories
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
                                     order_date=timezone.now(),
                                     status="In cart")
        order.products.add(order_product)
        msg = f"Product: {product.name} is added to your cart."
        return redirect('cart')

@login_required()
def cart(request):
    is_get_form = True
    order = Order.objects.filter(user=request.user, ordered=False).first()
    order_products = [] 
    form = ProductQuantityForm()
    if request.method == "POST":
        form = ProductQuantityForm(request.POST)
        is_get_form = False
        if form.is_valid():
            product_slug = request.POST.get('product_slug')
            product = get_object_or_404(Product, slug=product_slug)
            order_product = OrderProduct.objects.get(user=request.user,
                                                     ordered=False,
                                                     product=product)
            order_product.quantity = request.POST.get('quantity')
            order_product.save()
            msg = f"Product: {product.name} quantity is updated."
            messages.info(request, msg)
            return redirect('cart')
        else:
            msg = "Quantity is invalid"
            messages.info(request, msg)
    if order:
        order_products = order.get_user_order_products(request.user).order_by("order")
    paginator = Paginator(order_products, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "form": form,
        "order_products": page_obj,
        "is_get_form": is_get_form,
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
    is_get_form = True

    if request.method == "POST":
        form = ConfirmOrderForm(request.POST)
        is_get_form = False
        if form.is_valid():
            # Process the form if it's valid
            order = Order.objects.filter(user=request.user, ordered=False).first()
            cleaned_data = form.cleaned_data

            order.receiver_name = cleaned_data.get('receiver_name')
            order.receiver_surname = cleaned_data.get('receiver_surname')
            order.phone = cleaned_data.get('phone')
            order.address = cleaned_data.get('address')
            order.status = "Ordered"

            order.ordered = True
            order.save()
            messages.success(request, "Order successfully placed.")
            subject = 'Order Confirmation'
            email = request.user.email
            message = f'We\' received your order.'
            
            send_mail(subject, message, 'symmetrical_cart@example.com', [email], fail_silently=False)
            return redirect('cart')
        else:
            # If the form is invalid, display an error message
            messages.error(request, "Form is invalid.")
    else:
        # If it's a GET request, initialize a clean form
        initial = {
            'receiver_name': request.user.name,
            'receiver_surname': request.user.surname,
            'phone': request.user.phone,
            'address': request.user.address,
        }
        form = ConfirmOrderForm(initial=initial)

    context = {
        'order': order,
        'order_products': order_products,
        'form': form,
        'is_get_form': is_get_form,
    }
    return render(request, 'cart/checkout.html', context)

@login_required()
def rate_delivery(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = RateDeliveryForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            order.delivery_rate = rating 
            order.rated_by_user = True

            # Calculate average rating for the employee
            employee = order.delivery
            delivered_orders = Order.objects.filter(delivery=employee, rated_by_user=True)
            avg_rating = delivered_orders.aggregate(Avg('delivery_rate'))['delivery_rate__avg']

            # Update the employee's ratings with the calculated average
            employee.ratings = avg_rating
            employee.save()
            order.save()
            return redirect('profile')
        else:
            messages.error(request, 'Invalid rating.')
    return redirect('profile')




