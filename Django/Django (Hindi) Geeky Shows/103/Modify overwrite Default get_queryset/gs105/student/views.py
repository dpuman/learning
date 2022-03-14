from django.shortcuts import render

from student.models import Student

# Create your views here.


def home(request):
    student_data = Student.objects.all()
    # student_data = Student.student.all()
    context = {'students': student_data}
    return render(request, 'student/index.html', context)
