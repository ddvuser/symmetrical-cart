from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from .forms import RegisterForm, LoginForm

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
def user_profile(request):
    return render(request, 'profile.html') 
