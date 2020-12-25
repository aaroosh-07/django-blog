from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import ToDoList , Item
from .forms import CreateForm
from django.contrib.auth.models import User
from register.forms import UserForms , ProfileUpdateForm
# Create your views here.

def index(response,id):
    l = ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        t=response.POST.get("item")
        if len(t) > 2:
            l.item_set.create(text = t, name = response.user)
    else:
        pass
    return render(response,"main/view2.html",{"ls":l})

def home(response):
    context={
        'posts':ToDoList.objects.all(),
    }
    return render(response , "main/view1.html" ,context)

def create(response):
    
    if response.user.is_authenticated == False:
        return render(response,"register/login.html",{}) 
    if response.method == "POST":
        form = CreateForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t1 = form.cleaned_data["content"]
            t = ToDoList(name = n,content = t1,author = response.user)
            t.save()
    else:
        pass
    form = CreateForm()
    return render(response , "main/create.html" ,{"form":form})

def profile(response , username):
    u = User.objects.get(username=username)
    posts = u.todolist_set.all()
    content={
        'u':u,
        'posts':posts
    }
    return render(response , "main/profile2.html",content)

def update(response,id): 
    
    obj = ToDoList.objects.get(id = id)
    form = CreateForm()
    form.name = obj.name
    form.content = obj.content
    print(form)
    if response.method == "POST":
        form = CreateForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t1 = form.cleaned_data["content"]
            obj.name = n1
            obj.content = t1
            obj.save()
    else:
        pass
    
    return render(response , "main/create.html" ,{"form":form})


def edit(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            u_form = UserForms(response.POST , instance = response.user)
            u_profile = ProfileUpdateForm(response.POST , response.FILES , instance = response.user.profile)
            if u_form.is_valid() and u_profile.is_valid():
                u_form.save()
                u_profile.save()
                messages.success(response, f'Your account has been updated!')
                return redirect(profile , response.user.get_username())
        else:
            u_form = UserForms(instance = response.user)
            u_profile = ProfileUpdateForm(instance = response.user.profile)
            content = {
                'u_form':u_form,
                'u_profile':u_profile
            }
            return render(response , "main/edit.html",content)
    else:
        return redirect(home)

