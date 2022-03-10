from dataclasses import field
from importlib import import_module
from django import forms
from django.forms import ModelForm
from .models import employee


class StudentRegistration(ModelForm):
    # Extra Validation
    name = forms.CharField(max_length=76, required=False)

    class Meta:
        model = employee
        fields = ['name', 'email', 'password']
        labels = {'name': 'Your Name', 'email': 'Your Email'}
        error_messages = {'name': {'required': 'Enter Your Name Bro'}}
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name',
                                           'class': 'my-Class u-class'
                                           })
        }
