from django.shortcuts import render
from .models import Student
# Create your views here.


def index(request):
    try:
        oneStudent = Student.objects.get(pk=1)
    except:
        oneStudent = False
    stu = Student.objects.all()
    context = {'oneStudent': oneStudent, 'stu': stu}

    return render(request, 'enroll/index.html', context)
