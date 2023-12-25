from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_index, name='delivery_index'),
]
