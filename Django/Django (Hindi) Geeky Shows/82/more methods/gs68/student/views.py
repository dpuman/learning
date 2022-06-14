from email.policy import default
from urllib import response
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.


def setsession(request):
    request.session['name'] = 'Dipu'
    request.session['lname'] = 'Barman'
    request.session.set_expiry(600)
    # request.session.set_expiry(0)
    return render(request, 'student/setsession.html')


def getsession(request):
    name = request.session['name']
    lname = request.session.get('lname', default='Guest')

    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())

    context = {
        'name': name,
        'lname': lname,


    }
    return render(request, 'student/getsession.html', context)


def deletesession(request):
    # if 'name' in request.session:
    #     del request.session['name']

    request.session.flush()
    request.session.clear_expired()

    return render(request, 'student/deletesession.html')
