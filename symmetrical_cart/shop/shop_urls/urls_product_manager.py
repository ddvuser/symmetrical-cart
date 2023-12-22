from django.urls import path
from .. import main_views

urlpatterns = [
    path("", main_views.index, name='index'),

    path("product/<slug:slug>/",      
         main_views.product_detail,
         name='product_detail'),

    path("cart/", main_views.cart, name="cart"),

    path("add-to-cart/<slug:product_slug>", 
        main_views.add_to_cart, 
        name='add_to_cart'),

    path("remove-from-cart/<int:orderproduct_id>", 
        main_views.remove_from_cart, 
        name='remove_from_cart'),

    path('checkout/', main_views.checkout, name="checkout"),

    path("category/", 
         main_views.category, 
         name='category'),

    path("category/<slug:category_slug>", 
         main_views.category_detail, 
         name='category_detail'),

]
