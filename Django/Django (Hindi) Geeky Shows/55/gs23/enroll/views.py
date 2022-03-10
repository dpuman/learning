from django.shortcuts import render
from .models import Student
from .forms import StudentRegistration
# Create your views here.


# def index(request):
#     try:
#         oneStudent = Student.objects.get(pk=1)
#     except:
#         oneStudent = False
#     stu = Student.objects.all()
#     context = {'oneStudent': oneStudent, 'stu': stu}

#     return render(request, 'enroll/index.html', context)


def register(request):
    # fr = StudentRegistration(auto_id='my_%s', label_suffix=' :', initial={
    #                          'email': 'my@example.com'})

    # fr = StudentRegistration(initial={'name': 'Dipankar'})
    fr = StudentRegistration()

    return render(request, 'enroll/student-register.html', {'form': fr})
