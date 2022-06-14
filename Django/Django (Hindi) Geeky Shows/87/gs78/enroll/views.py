from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.


@cache_page(20)
def home(request):
    return render(request, 'enroll/home.html')


def course(request):
    return render(request, 'enroll/course.html')


def me(request):
    return HttpResponse('HELLO DIPU')
