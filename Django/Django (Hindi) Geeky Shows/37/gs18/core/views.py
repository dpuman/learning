from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html', {'d': 'Django 3.4'})


def about(request):
    return render(request, 'core/about.html')
