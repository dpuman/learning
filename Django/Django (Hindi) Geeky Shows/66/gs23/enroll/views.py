
from django.shortcuts import render

# Create your views here.


def home(request, check):
    return render(request, 'enroll/home.html', {'ok': check})


# def show(request, my_id):
#     return render(request, 'enroll/show.html', {'id': my_id})

def show(request, my_id=1):
    context = {}
    if my_id == 1:
        context = {'name': 'dipu', }
    elif my_id == 2:
        context = {'name': 'Apu'}
    elif my_id == 3:
        context = {'name': 'Topu'}

    return render(request, 'enroll/show.html', context)


def showDetails(request, my_id, info):

    if my_id == 1 and info == 4:
        context = {'name': 'dipu', 'roll': 1234}
    elif my_id == 2 and info == 5:
        context = {'name': 'Apu', 'roll': 5469}
    elif my_id == 3 and info == 6:
        context = {'name': 'Topu', 'roll': 231}

    return render(request, 'enroll/show.html', context)
