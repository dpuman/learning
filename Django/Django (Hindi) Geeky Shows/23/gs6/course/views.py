from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myCourse(request):
    return HttpResponse('My Course')


def myCourseDetails(request):
    return HttpResponse('My Course Details')
