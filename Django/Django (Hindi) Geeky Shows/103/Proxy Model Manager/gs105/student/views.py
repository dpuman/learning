from django.shortcuts import render

from student.models import Student, MyStudent

# Create your views here.


def home(request):

    # student_data = Student.objects.all()

    # student_data = MyStudent.student.all()
    student_data = MyStudent.student.get_stu_by_range(102, 107)

    context = {'students': student_data}
    return render(request, 'student/index.html', context)
