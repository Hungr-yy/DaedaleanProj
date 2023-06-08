from django.shortcuts import render
from django.http import HttpResponse
from .grading import *
import re

# Create your views here.

'''
def index(request):
    # name = 'Alphonsus' # Can be extracted from a database e.g. user.name
    context = { # context as a dictionary
        'name': 'Alphonsus',
        'location': 'Bishan'
    }
    return render(request, 'index.html', context)
'''

def index(request):
    return render(request, 'index.html')

'''
def result(request):
    text = request.POST['text']

    word_count, fre, fkra, fog, cli, smog, ari = grading(text)

    return render(request, 'result.html', {'text': text, 'word_count': word_count, 'fre': fre, 'fkra': fkra, 'fog': fog, 'cli': cli, 'smog': smog, 'ari': ari})
'''

def result(request):
    text = None

    if request.method == 'POST':
        text = request.POST.get('text')

    if len(text.split()) == 0:
        exception_string = "No words detected!"
        return render(request, 'index.html', {'exception_string': exception_string})
    elif ((text.count('.') + text.count('!') + text.count('?')) == 0 and len(text.split()) != 0):
        exception_string = "No sentences detected!"
        return render(request, 'index.html', {'exception_string': exception_string})
    else:
        word_count, fre, fkra, cli, smog, ari = grading(text)
        return render(request, 'index.html', {'text': text, 'word_count': word_count, 'fre': fre, 'fkra': fkra, 'cli': cli, 'smog': smog, 'ari': ari})