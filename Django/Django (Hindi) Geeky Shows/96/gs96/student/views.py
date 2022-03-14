from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
# Create your views here.


def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=60)

    # student_data = Student.objects.exclude(marks=60)

    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('name')

    # student_data = Student.objects.order_by('id').reverse()
    # student_data = Student.objects.order_by('id').reverse()[: 2]

    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'roll')

    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('name', 'roll')
    # student_data = Student.objects.values_list('name', 'roll', named=True)

    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates('pass_date', 'year')
    # student_data = Student.objects.dates('pass_date', 'month')
    # student_data = Student.objects.dates('pass_date', 'day')

    # q1 = Student.objects.values('id', 'name')
    # q2 = Teacher.objects.values('id', 'name')
    # student_data = q2.union(q1)
    # student_data = q2.union(q1, all=True)

    # q1 = Student.objects.values('id', 'name')
    # q2 = Teacher.objects.values('id', 'name')
    # student_data = q2.intersection(q1)

    # q1 = Student.objects.values('id', 'name')
    # q2 = Teacher.objects.values('id', 'name')
    # student_data = q2.difference(q1)

    ####### And Or operators #######

    # student_data = Student.objects.filter(
    #     id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    # student_data = Student.objects.filter(
    #     id=6) | Student.objects.filter(roll=105)
    student_data = Student.objects.filter(Q(id=6) | Q(roll=105))

    print('Result: ', student_data)
    print()
    print('SQL :', student_data.query)
    context = {'students': student_data}

    return render(request, 'student/home.html', context)
