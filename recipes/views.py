from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Renan Matias',
    })


def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse('<h1>SOBRE 1</h1>')
