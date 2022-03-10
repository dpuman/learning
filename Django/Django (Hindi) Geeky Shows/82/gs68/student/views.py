from email.policy import default
from urllib import response
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


def setsession(request):
    request.session['name'] = 'Dipu'
    request.session['lname'] = 'Barman'
    return render(request, 'student/setsession.html')


def getsession(request):
    name = request.session['name']
    lname = request.session.get('lname', default='Guest')

    return render(request, 'student/getsession.html', {'name': name, 'lname': lname})


def deletesession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/deletesession.html')
