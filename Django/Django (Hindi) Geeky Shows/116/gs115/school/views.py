import imp
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django import forms


class UpdateStudent(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thankyou/'


class SuccessView(TemplateView):
    template_name = 'school/thankyou.html'
