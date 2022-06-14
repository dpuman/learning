from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):
    student_data = Student.objects.get(pk=1)

    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date')

    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.all()
    # print(student_data.exists())
    # student_data = Student.objects.get(pk=1)
    # print(Student.objects.filter(pk=student_data.pk).exists())

    # student_data = Student.objects.create(
    #     name='Dipu', roll=107, city='Dhaka', marks=90, pass_date='2022-5-4')

    # student_data, created = Student.objects.get_or_create(
    #     name='Moni', roll=108, city='Dhaka', marks=95, pass_date='2022-5-4')
    # print(created)

    # student_data = Student.objects.filter(id=2).update(
    #     name='Ratul', city='Dhaka', marks=89)
    # student_data = Student.objects.filter(marks=60).update(
    #     city='Pass')

    # student_data, created = Student.objects.update_or_create(
    #     id=8, name='Moni', defaults={'name': 'Tamanna'})
    # print(created)

    # objs = [
    #     Student(name='Anik', roll=109, city='Dhaka',
    #             marks=100, pass_date='2022-5-4'),
    #     Student(name='Topu', roll=110, city='Dhaka',
    #             marks=99, pass_date='2022-5-4'),
    #     Student(name='Nipun', roll=111, city='Dhaka',
    #             marks=98, pass_date='2022-5-4'),
    # ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Dinajpur'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2])
    # print('Bulk:', student_data[1])
    # student_data = Student.objects.in_bulk([])
    # student_data = Student.objects.in_bulk()

    # student_data=Student.objects.all().delete()
    # student_data = Student.objects.get(pk=8).delete()
    # student_data = Student.objects.filter(marks=90).delete()

    # student_data = Student.objects.all()
    # print(student_data.count())

    print('Result: ', student_data)

    context = {'stu': student_data}

    return render(request, 'student/home.html', context)
