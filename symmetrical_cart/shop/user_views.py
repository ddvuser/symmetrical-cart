from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from .forms import RegisterForm, LoginForm, CustomPasswordChangeForm, EditUserForm, RateDeliveryForm
from .models import Order
from django.core.paginator import Paginator
import random
import string
from django.contrib import messages
from django.core.mail import send_mail

def user_register(request):
    is_get_form = True
    form = RegisterForm()
    if request.method == 'POST':
        is_get_form = False
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register success
            form.save()
            messages.success(request, 'You are successfully registered.')
            return redirect('login')
        else:
            # Register error
            msg = "Invalid credentials."
            messages.error(request, msg)

    context = {
        'form':form,
        'is_get_form': is_get_form,
    }
    return render(request, 'registration/register.html', context)

def user_login(request):
    is_get_form = True
    form = LoginForm()
    if request.method == 'POST':
        is_get_form = False
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                # Login success
                login(request, user)
                messages.success(request, 'You are logged in.')
                return redirect('profile')
            else:
                # Login error
                messages.error(request, 'Incorrect credentials.')
    context = {
        'form': form,
        'is_get_form': is_get_form,
    }
    return render(request, 'registration/login.html', context)

def user_logout(request):
    try:
        logout(request)
        messages.success(request, 'You are logged out.')
    except:
        message.error(request, 'Something went wrong...')
    return redirect('login')

@login_required()
def user_change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Password change success
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated.")
            return redirect('profile')
        else:
            # Password change error
            messages.error(request, "Incorrect credentials.")
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change-password/change_password.html', {'form':form})

@login_required(login_url='login')
def init_email_change(request):
    if request.method == 'POST':
        code = ''.join(random.choices(string.digits, k=6))  # Generate a 6-digit code
        request.session['email_change_code'] = code  # Store the code in the session
        request.session['input_code_attempts'] = 3
        email = request.user.email 

        # Send the code to the user's current email address
        subject = 'Email Verification Code'
        message = f'''
            Subject: {subject}

            Hello {email},

            You have initiated a request to change your email address. To complete this process, please use the following verification code:

            Verification Code: {code}

            Please enter this code on the verification page to confirm your email address change. If you did not initiate this change, please disregard this email.

            Thank you for using our service.

            Sincerely,
            Symmetrical Cart 
        '''
        # Send the email with the verification code to the user's current email address
        send_mail(subject, message, 'your_email@example.com', [email], fail_silently=False)
        return redirect('verify_email_change')
    return render(request, 'email-change/init_email_change.html')

@login_required(login_url='login')
def verify_email_change(request):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')
        stored_code = request.session.get('email_change_code')
        attempts = request.session.get('input_code_attempts')
        if entered_code == stored_code:
            # Code verification successful, allow the user to submit a new email
            return redirect('submit_new_email')
        else:
            if attempts > 0:
                request.session['input_code_attempts'] -= 1
                msg = f"Incorrect Code. {attempts} attempts left."
                messages.error(request, msg)
            else:
                msg = "Incorrect Code. No attempts left." 
                messages.error(request, msg)
                return redirect('profile')
    return render(request, 'email-change/verify_email_change.html')

@login_required(login_url='login')
def submit_new_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('new_email')

        # Update the user's email address in the database
        request.user.email = new_email
        request.user.save()

        # Clear the email change code from the session
        request.session.pop('email_change_code', None)
        messages.success(request, "Email updated.")
        return redirect('profile')

    return render(request, 'email-change/submit_new_email.html')

@login_required()
def user_profile(request):
    is_get_form = True
    if request.method == "POST":
        is_get_form = False
        form = EditUserForm(request.POST)
        if form.is_valid():
            if form.has_changed():
                user = request.user
                user.name = form.cleaned_data["name"]
                user.surname = form.cleaned_data["surname"]
                user.phone = form.cleaned_data["phone"]
                user.address = form.cleaned_data["address"]
                user.save()

                messages.info(request, "You have updated your data.")
            return redirect('profile')
        else:
            messages.error(request, "Invalid form data.")
    else:
        initial = {
            'name': request.user.name,
            'surname': request.user.surname,
            'phone': request.user.phone,
            'address': request.user.address,
        }
        form = EditUserForm(initial)

    orders = Order.objects.filter(user=request.user, ordered=True).order_by("-created_date")
    paginator = Paginator(orders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    rate_form = RateDeliveryForm()

    context = {
        'orders': page_obj,
        'form': form,
        'is_get_form': is_get_form,
        'rate_form': rate_form,
    }
    return render(request, 'profile.html', context)
