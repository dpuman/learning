from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from datetime import date, time
# Create your views here.


def home(request):

    student_data = Student.objects.all()
    student_data = Student.objects.filter(name__exact='sonam')
    student_data = Student.objects.filter(name__iexact='Sonam')

    student_data = Student.objects.filter(name__contains='u')
    student_data = Student.objects.filter(name__icontains='u')

    student_data = Student.objects.filter(id__in=[2, 5, 1])
    student_data = Student.objects.filter(marks__in=[60, 80])

    student_data = Student.objects.filter(marks__gt=60)
    student_data = Student.objects.filter(marks__gte=60)

    student_data = Student.objects.filter(marks__lt=60)
    student_data = Student.objects.filter(marks__lte=60)

    student_data = Student.objects.filter(name__startswith='s')
    student_data = Student.objects.filter(name__istartswith='S')

    student_data = Student.objects.filter(name__endswith='l')
    student_data = Student.objects.filter(name__iendswith='L')

    student_data = Student.objects.filter(
        pass_date__range=('2022-03-08', '2022-03-10'))

    student_data = Student.objects.filter(
        admdatetime__date=date(2022, 3, 15))
    student_data = Student.objects.filter(
        admdatetime__date__gt=date(2022, 3, 15))

    student_data = Student.objects.filter(
        pass_date__year=2022)
    student_data = Student.objects.filter(
        pass_date__year__gt=2021)

    student_data = Student.objects.filter(
        pass_date__month=3)
    student_data = Student.objects.filter(
        pass_date__month__gte=3)

    student_data = Student.objects.filter(
        pass_date__day=10)
    student_data = Student.objects.filter(
        pass_date__day__gte=10)

    student_data = Student.objects.filter(
        pass_date__week=9)
    student_data = Student.objects.filter(
        pass_date__week__gt=9)

    student_data = Student.objects.filter(
        pass_date__week_day=4)
    student_data = Student.objects.filter(
        pass_date__week_day__gt=4)

    student_data = Student.objects.filter(
        pass_date__quarter=1)

    student_data = Student.objects.filter(
        admdatetime__time__gt=time(6, 00))

    student_data = Student.objects.filter(
        admdatetime__hour__gt=5)
    student_data = Student.objects.filter(
        admdatetime__minute__gt=2)

    student_data = Student.objects.filter(
        roll__isnull=True)
    student_data = Student.objects.filter(
        roll__isnull=False)

    print('Result: ', student_data)
    print()
    print('SQL :', student_data.query)
    context = {'students': student_data}

    return render(request, 'student/home.html', context)
