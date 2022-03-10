from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Home View')


def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')


def learn_math(request):
    a = 10+20
    return HttpResponse(a)


def learn_format(request):
    a = 10+20
    return HttpResponse(f'Hello Man{a}')
