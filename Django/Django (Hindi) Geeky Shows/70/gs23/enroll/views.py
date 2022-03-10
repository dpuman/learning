
from django.shortcuts import render
from .forms import TeacherRegistration, NewStudentRegistration
# Create your views here.


def teacher(request):

    if request.method == 'POST':
        fr = TeacherRegistration(request.POST)
        if fr.is_valid():
            fr.save()
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
