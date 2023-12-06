from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from .forms import RegisterForm, LoginForm, CustomPasswordChangeForm
import random
import string
from django.core.mail import send_mail

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                # Login success
                login(request, user)
                return redirect('profile')
            else:
                # Login error TODO
                ...
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required()
def user_change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'change-password/change_password.html', {'form':form})

@login_required(login_url='login')
def init_email_change(request):
    if request.method == 'POST':
        code = ''.join(random.choices(string.digits, k=6))  # Generate a 6-digit code
        request.session['email_change_code'] = code  # Store the code in the session
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
            PassVault 
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
        if entered_code == stored_code:
            # Code verification successful, allow the user to submit a new email
            return redirect('submit_new_email')
        else:
            ...
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

        return redirect('profile')

    return render(request, 'email-change/submit_new_email.html')

@login_required()
def user_profile(request):
    return render(request, 'profile.html') 
