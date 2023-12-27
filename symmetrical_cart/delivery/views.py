from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Order, Category
from .models import Employee
from django.core.paginator import Paginator
from .filters import OrderFilter 
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

@login_required()
def delivery_index(request):
    if not request.user.is_employee:
        return redirect('index')

    order_filter = OrderFilter(
        request.GET,
        Order.objects.filter(Q(status="Ordered") | Q(status="Taken")).order_by("-order_date")
    )
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

@login_required()
def decline_order(request, order_id):
    employee = get_object_or_404(Employee, user=request.user)

    if not request.user.is_employee or not employee:
        return redirect('index')

    order = get_object_or_404(Order, id=order_id)
    if not order:
        return redirect('delivery_index')

    if order in employee.current_orders.all():
        order.delivery = None
        order.status = "Ordered"
        employee.current_orders.remove(order)
        order.save()
        messages.info(request, "Order declined.")
    else:
        messages.info(request, "You did not take this order.")

    return redirect('delivery_index')

@login_required()
def complete_order(request, order_id):
    employee = get_object_or_404(Employee, user=request.user)

    if not request.user.is_employee or not employee:
        return redirect('index')

    order = get_object_or_404(Order, id=order_id)
    if not order:
        return redirect('delivery_index')

    if order in employee.current_orders.all():
        order.status = "Delivered"
        order.delivered_date = timezone.now()
        order.save()
        messages.info(request, "You've completed this order.")
    else:
        messages.info(request, "You did not take this order.")

    return redirect('delivery_index')

@login_required()
def my_orders(request):
    employee = get_object_or_404(Employee, user=request.user)
    if employee:
        current_orders = Order.objects.filter(delivery=employee, status="Taken").order_by("-order_date")
        delivered_orders = Order.objects.filter(delivery=employee, status="Delivered").order_by("-order_date")

        current_orders_paginator = Paginator(current_orders, 10)
        current_orders_page_number = request.GET.get("current_page")
        current_orders_page_obj = current_orders_paginator.get_page(current_orders_page_number)

        delivered_orders_paginator = Paginator(delivered_orders, 10)
        delivered_orders_page_number = request.GET.get("delivered_page")
        delivered_orders_page_obj = delivered_orders_paginator.get_page(delivered_orders_page_number)

        context = {
            "current_orders": current_orders_page_obj,
            "delivered_orders": delivered_orders_page_obj,
        }
        
        return render(request, 'my_orders.html', context)


