from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def myFees(request):
#     return HttpResponse('Hello')

def myFees(request):
    return render(request, 'fees/fees-one.html')
