from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'gen/home.html',)


def generate(request):
    thepassword = 'test'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase',):
        characters.extend(list('ABCDEFGHIJKLMNOPQRTUVWXYZ'))

    if request.GET.get('special',):  # name
        characters.extend(list('!@#$%&*()'))

    if request.GET.get('numbers',):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'gen/generate.html', {'password': thepassword})


def about(request):
    return render(request, 'gen/about.html')
