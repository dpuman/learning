import imp
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django import forms


# class DeleteStudent(DeleteView):
#     model = Student
#     success_url = '/thankyou/'

class DeleteStudent(DeleteView):
    model = Student
    template_name = 'school/delete.html'

    success_url = '/thankyou/'


class SuccessView(TemplateView):
    template_name = 'school/thankyou.html'
