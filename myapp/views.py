from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .grading import *
import re
import html

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already in use.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This username is already in use.')
                return redirect('register')
            elif len(password) < 8:
                messages.info(request, 'Insufficient password length.')
                return redirect('register')
            else:
                user = User.object.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def result(request):
    text = None

    if request.method == 'POST':
        text = request.POST.get('text')

    pattern = r"<.*?>"
    text = html.unescape(text)
    text = re.sub(pattern, "", text)

    if len(text.split()) == 0:
        messages.info(request, 'No words detected!')
        return redirect('index')
    elif ((text.count('.') + text.count('!') + text.count('?')) == 0 and len(text.split()) != 0):
        messages.info(request, 'No sentences detected!')
        return redirect('index')
    elif text[0] == "!" or text[0] == "?" or text[0] == "." or text[0] == ",":
        messages.info(request, 'Invalid starting character!')
        return redirect('index')
    else:
        word_count, sentence_count, fre, fkra, cli, smog, ari = grading(text)
        return render(request, 'index.html', {'text': text, 'word_count': word_count, 'sentence_count': sentence_count, 'fre': fre, 'fkra': fkra, 'cli': cli, 'smog': smog, 'ari': ari})
