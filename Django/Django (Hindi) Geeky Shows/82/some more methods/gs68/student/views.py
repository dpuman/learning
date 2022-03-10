from email.policy import default
from urllib import response
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


def settestcookie(request):
    request.session.set_test_cookie()
    request.session['name'] = 'Dipu'
    return render(request, 'student/setsession.html')


def gettestcookie(request):
    print(request.session.test_cookie_worked())
    name = request.session.get('name')

    return render(request, 'student/getsession.html', {'name': name})


def deletetestcookie(request):
    request.session.delete_test_cookie()

    return render(request, 'student/deletesession.html')
