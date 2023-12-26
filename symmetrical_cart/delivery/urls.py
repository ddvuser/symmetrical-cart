from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_index, name='delivery_index'),
    path('accept_order/<int:order_id>', views.accept_order, name='accept_order'),
]
