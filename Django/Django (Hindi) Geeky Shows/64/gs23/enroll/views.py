from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentRegistration
# Create your views here.


def thankYou(request):

    return render(request, 'enroll/success.html')


def register(request):
    if request.method == 'POST':
        fr = StudentRegistration(request.POST)

        if fr.is_valid():
            id = fr.cleaned_data['student_id']
            name = fr.cleaned_data['name']
            email = fr.cleaned_data['email']
            passWord = fr.cleaned_data['password']
            comment = fr.cleaned_data['comments']
            print(id, name, email, passWord, comment)
            # SAVE
            # rg = Student(stuId=id, stuName=name, stuEmail=email,
            #              stuPassword=passWord, comments=comment)

            # rg.save()

            # UPDATE
            # rg = Student(id=5, stuId=id, stuName=name, stuEmail=email,
            #              stuPassword=passWord, comments=comment)
            # rg.save()

            # DELETE
            rg = Student(id=5)
            rg.delete()

    else:
        fr = StudentRegistration()

    return render(request, 'enroll/student-register.html', {'form': fr})
