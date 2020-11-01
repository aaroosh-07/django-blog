from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList , Item
from .forms import CreateForm
from django.contrib.auth.models import User
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
    return render(response , "main/profile.html",{'posts':posts})

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



