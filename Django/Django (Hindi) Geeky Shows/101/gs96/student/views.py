from django.shortcuts import render
from .models import Student


# Create your views here.


def home(request):

    student_data = Student.objects.all()[:4]
    student_data = Student.objects.all()[2:5]
    student_data = Student.objects.all()[::2]

    print('Result: ', student_data)
    print()
    # print('SQL :', student_data.query)
    context = {
        'students': student_data,

    }

    return render(request, 'student/home.html', context)
