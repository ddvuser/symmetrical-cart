from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_index, name='delivery_index'),
    path('accept-order/<int:order_id>', views.accept_order, name='accept_order'),
    path('decline-order/<int:order_id>', views.decline_order, name='decline_order'),
    path('complete-order/<int:order_id>', views.complete_order, name='complete_order'),

    path('my-orders/', views.my_orders, name='my_orders'),
]
