import imp
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django import forms


# class CreateStudent(CreateView):
#     model = Student
#     fields = ['name', 'roll', 'course']
#     success_url = '/thankyou/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(
#             attrs={'class': 'myclass'})
#         return form

class CreateStudent(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thankyou/'


class SuccessView(TemplateView):
    template_name = 'school/thankyou.html'
