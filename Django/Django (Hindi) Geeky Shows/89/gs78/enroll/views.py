from ensurepip import version
from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

# General
# def home(request):
#     cv = cache.get('name', 'No value Set')
#     if cv == 'No value Set':
#         cache.set('name', 'Dipankar', 30)
#         cv = cache.get('name')
#     return render(request, 'enroll/home.html', {'name': cv})

# Shortcut


def home(request):
    mv = cache.get_or_set('Movie', 'Gurray', 30)
    mv2 = cache.get_or_set('Movie', 'Titanic', 30, version=2)
    return render(request, 'enroll/home.html', {'name': mv, 'mv2': mv2})


# SET/GET MANY
# def home(request):
#     data = {
#         'name': 'Dipu',
#         'Roll': 101
#     }
#     cache.set_many(data, 30)
#     rv = cache.get_many(data)
#     return render(request, 'enroll/home.html', {'data': rv})

# Delete
# def home(request):
#     # cache.delete('name')
#     cache.delete('Movie', version=2)
#     return render(request, 'enroll/home.html')


# INC/DIC
# def home(request):
#     # cache.set('value', 100, 40)
#     # cache.decr('value', delta=2)
#     cache.incr('value', delta=2)
#     rv = cache.get('value')
#     return render(request, 'enroll/home.html', {'data': rv})

# clear all
# def home(request):
#     cache.clear()
#     return render(request, 'enroll/home.html')
