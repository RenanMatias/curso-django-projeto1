# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>HOME 1</h1>')


def contato(request):
    return HttpResponse('<h1>CONTATO 1</h1>')


def sobre(request):
    return HttpResponse('<h1>SOBRE 1</h1>')
