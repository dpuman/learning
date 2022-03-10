from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def myFees(request):
    return HttpResponse('My fees')


def myFeesDetails(request):
    return HttpResponse('My fees Details')
