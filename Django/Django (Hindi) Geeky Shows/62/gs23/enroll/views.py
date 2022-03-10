from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration
# Create your views here.


def thankYou(request):

    return render(request, 'enroll/success.html')


def register(request):
    if request.method == 'POST':
        fr = StudentRegistration(request.POST)

        if fr.is_valid():
            name = fr.cleaned_data['password']

    else:
        fr = StudentRegistration()

    return render(request, 'enroll/student-register.html', {'form': fr})
