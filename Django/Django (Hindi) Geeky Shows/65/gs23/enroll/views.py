from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student, employee
from .forms import StudentRegistration
# Create your views here.


def thankYou(request):

    return render(request, 'enroll/success.html')


def register(request):
    if request.method == 'POST':
        em = employee.objects.get(id=1)
        fr = StudentRegistration(request.POST, instance=em)

        if fr.is_valid():
            fr.save()

            # name = fr.cleaned_data['name']
            # email = fr.cleaned_data['email']
            # passWord = fr.cleaned_data['password']

            # print(name, email, passWord)
            # reg = employee(name=name, email=email, password=passWord)
            # reg = employee(id=1, name=name, email=email, password=passWord)
            # reg.save()
            # reg = employee(id=2)
            # reg.delete()

    else:
        fr = StudentRegistration()

    return render(request, 'enroll/student-register.html', {'form': fr})
