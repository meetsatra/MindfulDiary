from datetime import date
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url="/login")
def home(request):
    journal_entries = JournalEntry.objects.all()
    return render(request, "index.html", context = {'page':'Home','journal_entries': journal_entries})

@login_required(login_url="/login")
def add(request):
    if request.method == "POST":
        data = request.POST
        desc = data.get('desc')

        JournalEntry.objects.create(
            user=request.user,
            entry_text = desc,
            date=date.today(),
        )
        return redirect('/')
    return render(request, "add.html", context = {'page':'Add Journal'})

def login_page(request):
    if request.method == "POST":

        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if User.objects.filter(username = username).exists() == False:
            messages.error(request, f"Username '{username}' Doesnt exist. Please register")
            return redirect('/login')
        
        user = authenticate(username = username, password = password)
        # print(user)
        if user is None:
            messages.error(request, f"The password is incorrect")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/recipes')
    context = {'page':'Login'}
    return render(request, 'login.html', context)

def register(request): 
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, f"Username '{username}' already exists.")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            # password = password,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Successfully. Please login.")
        return redirect('/register')
    context = {'page':'register'}
    return render(request, 'register.html', context)

def logout_page(request):
    logout(request)
    return redirect('/login')