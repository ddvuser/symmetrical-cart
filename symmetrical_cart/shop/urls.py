from django.urls import path
from . import user_views

urlpatterns = [
    path("profile/", user_views.user_profile, name='profile'),
    path("register/", user_views.user_register, name='register'),
    path("login/", user_views.user_login, name='login'),
    path("logout/", user_views.user_logout, name='logout'),
]
