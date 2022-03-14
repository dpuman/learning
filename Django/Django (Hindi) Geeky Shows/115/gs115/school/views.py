import imp
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView


class CreateStudent(CreateView):
    model = Student
    fields = ['name', 'roll', 'course']
    # success_url = '/thankyou/'


class SuccessView(TemplateView):
    template_name = 'school/thankyou.html'


class StudentDetailView(DetailView):
    model = Student
