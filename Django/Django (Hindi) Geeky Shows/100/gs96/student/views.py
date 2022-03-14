from django.shortcuts import render
from .models import Student
from django.db.models import Q

# Create your views here.


def home(request):

    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))
    # student_data = Student.objects.filter(Q(id=6) | Q(roll=104))
    student_data = Student.objects.filter(~Q(id=6))

    print('Result: ', student_data)
    print()
    print('SQL :', student_data.query)
    context = {
        'students': student_data,

    }

    return render(request, 'student/home.html', context)
