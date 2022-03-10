from urllib import response
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'Dipu', salt='nm')

    return response


def getcookie(request):
    # name = request.get_signed_cookie('name',  salt='nm')
    name = request.get_signed_cookie('name', default='Guest', salt='nm')

    return render(request, 'student/getcookie.html', {'name': name})


def deletecookie(request):
    response = render(request, 'student/deletecookie.html')
    response.delete_cookie('name')
    return response
