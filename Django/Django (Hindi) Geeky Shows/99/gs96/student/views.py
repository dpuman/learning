from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Max, Min, Sum, Count

# Create your views here.


def home(request):

    student_data = Student.objects.all()

    average = student_data.aggregate(Avg('marks'))
    maximum = student_data.aggregate(Max('marks'))
    minimum = student_data.aggregate(Min('marks'))
    total = student_data.aggregate(Sum('marks'))
    total_count = student_data.aggregate(Count('marks'))

    print('Result: ', student_data)
    print()
    print('SQL :', student_data.query)
    context = {
        'students': student_data,
        "average": average,
        "maximum": maximum,
        "minimum": minimum,
        "total": total,
        "total_count": total_count,

    }

    return render(request, 'student/home.html', context)
