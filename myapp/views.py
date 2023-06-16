from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .grading import *
import re
import html

def index(request):

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
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if first_name == "" or last_name == "" or email == "" or password == "" or password2 == "":
            messages.info(request, 'Incomplete fields.')
            return redirect('register')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already in use.')
                return redirect('register')
            elif User.objects.filter(first_name=first_name, last_name=last_name).exists():
                messages.info(request, 'This name is already in use.')
                return redirect('register')
            elif len(password) < 8:
                messages.info(request, 'Password must be at least 8 characters long.')
                return redirect('register')
            else:
                user = User.object.create_user(first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Incorrect email or password.')
            return redirect ('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
