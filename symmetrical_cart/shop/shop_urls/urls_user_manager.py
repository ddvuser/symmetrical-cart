from django.urls import path
from ..user_views import *
from ..forms import CustomPasswordResetForm, CustomPasswordResetConfirmForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    
    # Password urls
    path("password-change", user_change_password, name='change_password'),

    path('password-reset/', 
            PasswordResetView.as_view(
                template_name='change-password/password_reset.html',
                form_class=CustomPasswordResetForm),
                name='password_reset'
         ),
    path('password-reset/done/', 
            PasswordResetDoneView.as_view(
                template_name='change-password/password_reset_done.html'),
                name='password_reset_done'
         ),
    path('password-reset-confirm/<uidb64>/<token>/', 
            PasswordResetConfirmView.as_view(
                template_name='change-password/password_reset_confirm.html',
                extra_context={'form': CustomPasswordResetConfirmForm()}),
                name='password_reset_confirm'
         ),
    path('password-reset-complete/',
            PasswordResetCompleteView.as_view(
                template_name='change-password/password_reset_complete.html'),
                name='password_reset_complete'
         ),

    # Email urls
    path('init-email-change/',init_email_change, name='init_email_change'),
    path('verify-email-change/', verify_email_change, name='verify_email_change'),
    path('submit-new-email/', submit_new_email, name='submit_new_email'),
    
    # Profile
    path("profile/", user_profile, name='profile'),
    # Register
    path("register/", user_register, name='register'),
    path("login/", user_login, name='login'),
    path("logout/", user_logout, name='logout'),



]
