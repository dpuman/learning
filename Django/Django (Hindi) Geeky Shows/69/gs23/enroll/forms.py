from dataclasses import field
from importlib import import_module
from django import forms
from django.forms import ModelForm
from .models import Employee


class StudentRegistration(ModelForm):
    # Extra Validation
    name = forms.CharField(max_length=76, required=False)

    class Meta:
        model = Employee
        exclude = ['password']
        # fields = ['name', 'email', 'password']
        # fields = '__all__'
