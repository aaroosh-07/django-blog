from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# Create your views here.

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(response , 'register/register.html' , {"form":form})

def getin(response):
    return render()

