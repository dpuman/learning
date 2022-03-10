from urllib import response
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name', 'Dipu')
    response.set_cookie('GF', 'Simran', max_age=10)
    response.set_cookie('Country', 'Bangladesh',
                        expires=datetime.now()+timedelta(days=2))
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'student/getcookie.html', {'name': name})


def deletecookie(request):
    response = render(request, 'student/deletecookie.html')
    response.delete_cookie('name')
    return response
