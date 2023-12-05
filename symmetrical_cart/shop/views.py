from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseBadRequest

def regiser(request):
    if request.method == 'POST':
        ...
    else:
        return render(request, 'registration/register.html')

def login(request):
    if request.method == 'POST':
        ...
    else:
        return render(request, 'registration/login.html')

def logout(request):
    ...

def profile(request):
    pass
