from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'enroll/home.html')


def course(request):
    return render(request, 'enroll/course.html')
