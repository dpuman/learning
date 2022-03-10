from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.


def home(request):
    print('This is Home View')
    return HttpResponse('This is Home Bro')


def excpt(request):
    print('This is Except View')
    a = 10/0
    return HttpResponse('This is Exception view Bro')


def tempContext(request):
    print('This is temp context View')
    context = {'name': 'Dipu'}
    return TemplateResponse(request, 'blog/context.html', context)
