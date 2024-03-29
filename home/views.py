from datetime import date
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .nlp import process_description  # Import the function from nlp.py
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

from gpt4all import GPT4All

model_path = r"D:\\LLM\\Downloads"
model_name = "mistral-7b-openorca2.Q4_0.gguf"

# Create your views here.
@login_required(login_url="/login")
def home(request):
    journal_entries = JournalEntry.objects.all().order_by('-date')
    return render(request, "index.html", context = {'page':'Home','journal_entries': journal_entries})

def delete_entry(request, entry_id):
    entry = get_object_or_404(JournalEntry, pk=entry_id)
    entry.delete()
    return redirect('/')

@login_required(login_url="/login")
def add(request):
    if request.method == "POST":
        data = request.POST
        desc = data.get('desc')
        generate_response = data.get('generateResponse') == 'on'

        model = GPT4All(model_name=model_name, model_path=model_path)

        # feedback = process_description(desc) if generate_response else ""
        feedback = model.generate(desc, max_tokens=200) if generate_response else ""
        print(desc)
        print(feedback)

        journal_entry = JournalEntry.objects.create(
            user=request.user,
            entry_text=desc,
            date=date.today(),
        )

        Feedback.objects.create(
            user=request.user,
            journal_entry=journal_entry,
            feedback_text=feedback,
        )
        return redirect('/')
    return render(request, "add.html", context = {'page':'Add Journal'})

@login_required(login_url="/login")
def chat(request):
    conversations = ChatbotConversation.objects.all()
    return render(request, "chat.html", {'page': 'Chat', 'conversations': conversations})

# Add a view to handle AJAX requests for sending messages
@login_required(login_url="/login")
def send_message(request):
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message')
        is_chatbot_message = False  # Assuming user messages are not from the chatbot

        conversation = ChatbotConversation.objects.create(
            user=user,
            message=message,
            is_chatbot_message=is_chatbot_message,
        )

        return JsonResponse({'status': 'success', 'message': conversation.message})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

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
            return redirect('/add')
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