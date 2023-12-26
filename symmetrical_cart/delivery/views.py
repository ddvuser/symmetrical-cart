from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Order, Category
from .models import Employee
from django.core.paginator import Paginator
from .filters import OrderFilter 
from django.contrib import messages

@login_required()
def delivery_index(request):
    if not request.user.is_employee:
        return redirect('index')

    order_filter = OrderFilter(request.GET, Order.objects.all().order_by("-order_date"))
    filtered_orders = order_filter.qs

    orders = Order.objects.filter(delivery=None)
    paginator = Paginator(filtered_orders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    employee = get_object_or_404(Employee, user=request.user)

    context = {
        "page_obj": page_obj,
        "order_filter": order_filter,
        "employee": employee,
    }
    return render(request, "delivery_index.html", context=context)

@login_required()
def accept_order(request, order_id):
    employee = get_object_or_404(Employee, user=request.user)

    if not request.user.is_employee or not employee:
        return redirect('index')

    order = get_object_or_404(Order, id=order_id)
    if not order:
        return redirect('delivery_index')

    # Check if the order is already assigned to the employee
    if order in employee.current_orders.all():
        messages.info(request, "Order already added.")
    else:
        order.status = "Taken"
        order.delivery = employee 
        order.save()
        employee.current_orders.add(order)
        messages.info(request, "Order added.")

    return redirect('delivery_index')
