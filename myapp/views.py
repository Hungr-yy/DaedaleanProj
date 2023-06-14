from django.shortcuts import render
from django.http import HttpResponse
from .grading import *
import re
import html

def index(request):
    return render(request, 'index.html')

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
        exception_string = "No words detected!"
        return render(request, 'index.html', {'exception_string': exception_string})
    elif ((text.count('.') + text.count('!') + text.count('?')) == 0 and len(text.split()) != 0):
        exception_string = "No sentences detected!"
        return render(request, 'index.html', {'exception_string': exception_string})
    elif text[0] == "!" or text[0] == "?" or text[0] == "." or text[0] == ",":
        exception_string = "Invalid starting character!"
        return render(request, 'index.html', {'exception_string': exception_string})
    else:
        word_count, sentence_count, fre, fkra, cli, smog, ari = grading(text)
        return render(request, 'index.html', {'text': text, 'word_count': word_count, 'sentence_count': sentence_count, 'fre': fre, 'fkra': fkra, 'cli': cli, 'smog': smog, 'ari': ari})
