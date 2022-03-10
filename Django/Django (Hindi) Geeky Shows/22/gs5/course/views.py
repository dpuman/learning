from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def my_course(request):
    return HttpResponse("MY Course")
