from email.policy import default
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


def setsession(request):
    request.session['name'] = 'Dipu'

    return render(request, 'student/setsession.html')


def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        context = {
            'name': name,
        }
        return render(request, 'student/getsession.html', context)
    else:
        return HttpResponse("Session expired")


def deletesession(request):

    request.session.flush()
    request.session.clear_expired()

    return render(request, 'student/deletesession.html')
