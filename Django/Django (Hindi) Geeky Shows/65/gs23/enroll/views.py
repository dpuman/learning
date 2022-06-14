from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student, employee
from .forms import EmployeeRegistration
# Create your views here.


def thankYou(request):

    return render(request, 'enroll/success.html')


def register(request):
    if request.method == 'POST':

        fr = EmployeeRegistration(request.POST)
        # UPDATE
        # em = employee.objects.get(id=1)
        # fr = EmployeeRegistration(request.POST, instance=em)

        if fr.is_valid():
            # UPDATE/SAVE
            fr.save()

            # name = fr.cleaned_data['name']
            # email = fr.cleaned_data['email']
            # passWord = fr.cleaned_data['password']

            # print(name, email, passWord)
            # reg = employee(name=name, email=email, password=passWord)
            # reg = employee(id=1, name=name, email=email, password=passWord)
            # reg.save()

            # DELETE
            # reg = employee(id=3)
            # reg.delete()

    else:
        fr = EmployeeRegistration()

    return render(request, 'enroll/student-register.html', {'form': fr})
