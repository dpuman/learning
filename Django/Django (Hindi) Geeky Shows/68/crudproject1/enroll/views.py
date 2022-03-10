from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from . forms import StudentForm
from . models import Student
# Create your views here.


def home(request):
    if request.method == 'POST':
        fr = StudentForm(request.POST)
        if fr.is_valid():
            name = fr.cleaned_data['name']
            email = fr.cleaned_data['email']
            password = fr.cleaned_data['password']
            reg = Student(name=name, email=email, password=password)
            reg.save()
            fr = StudentForm()
    else:
        fr = StudentForm()
    st = Student.objects.all()
    return render(request, 'enroll/home.html', {'form': fr, 'st': st})


def deleteStudent(request, id):
    data = Student.objects.get(pk=id)
    data.delete()
    return redirect('home')


def updateStudent(request, id):
    st = Student.objects.get(pk=id)
    if request.method == "POST":
        fr = StudentForm(request.POST, instance=st)
        if fr.is_valid():
            fr.save()
    else:
        fr = StudentForm(instance=st)
    return render(request, 'enroll/update.html', {'form': fr})
