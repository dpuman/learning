
from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def show(request):
    fr = StudentRegistration()
    return render(request, 'enroll/show.html', {'form': fr})
