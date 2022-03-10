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

    keys = request.session.keys()
    items = request.session.items()

    defaults = request.session.setdefault('age', '27')
    context = {
        'name': name,
        'lname': lname,
        'keys': keys,
        'items': items,
        'defaults': defaults,

    }
    return render(request, 'student/getsession.html', context)


def deletesession(request):
    # if 'name' in request.session:
    #     del request.session['name']

    request.session.flush()
    return render(request, 'student/deletesession.html')
