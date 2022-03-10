
from django.shortcuts import render
from django.contrib import messages
from .forms import TeacherRegistration, NewStudentRegistration
# Create your views here.


def teacher(request):

    if request.method == 'POST':
        fr = TeacherRegistration(request.POST)
        if fr.is_valid():
            fr.save()
            print(messages.get_level)
            messages.add_message(request, messages.SUCCESS, 'OKay created')
            messages.info(request, 'Info OKay created')
            messages.error(request, 'Error BRO')
            messages.debug(request, 'DEBUG')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'DEBUG OKAY')
    else:
        fr = TeacherRegistration()
    return render(request, 'enroll/teacher.html', {'form': fr})


def student(request):
    if request.method == 'POST':
        fr = NewStudentRegistration(request.POST)
        if fr.is_valid():
            fr.save()
    else:
        fr = NewStudentRegistration()
    return render(request, 'enroll/student.html', {'form': fr})
