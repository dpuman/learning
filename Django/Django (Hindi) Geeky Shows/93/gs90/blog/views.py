from django.http import HttpResponse
from django.shortcuts import render
from blog import signals
# Create your views here.


def home(request):
    signals.notification.send(
        sender=None, request=request, user=['Dipu', 'Moni'])
    return HttpResponse('<h1>Hello signal bro</h1>')
