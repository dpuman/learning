from django.shortcuts import render

from student.models import Student

# Create your views here.


def home(request):

    #This is custom
    student_data = Student.student.get_stu_by_range(101, 105)

    # get_queryset() will work fine
    # student_data = Student.student.all()

    context = {'students': student_data}
    return render(request, 'student/index.html', context)
