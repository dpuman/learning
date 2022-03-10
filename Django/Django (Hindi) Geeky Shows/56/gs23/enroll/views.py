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
    if request.method == 'POST':
        fr = StudentRegistration(request.POST)
        print('POST')
        print(fr)
        if fr.is_valid():
            print('Valid Post')
            print(fr.cleaned_data)
            name = fr.cleaned_data['name']
            email = fr.cleaned_data['email']
            password = fr.cleaned_data['password']
            print(name)
            print(email)
            print(password)
            # Not recomended
            myName = request.POST['name']
            print(myName)

    else:
        fr = StudentRegistration()

    return render(request, 'enroll/student-register.html', {'form': fr})
