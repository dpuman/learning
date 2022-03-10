from django.shortcuts import render

# Create your views here.


def myFees(request):
    return render(request, 'fees/info.html', {'Name': 'myFees'})
