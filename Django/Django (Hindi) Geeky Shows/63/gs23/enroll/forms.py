
from distutils.command.clean import clean
# from wsgiref.validate import validator
from django import forms
# from django.core import validators

# without required
# class StudentRegistration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

# with required


class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter your Name'},
                           max_length=10, min_length=2)
    email = forms.EmailField(
        error_messages={'required': 'Enter your Email'}, max_length=20, min_length=5)
    password = forms.CharField(widget=forms.PasswordInput)

# with error_css_class/required_css_clsss


class StudentRegistration(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    name = forms.CharField(error_messages={'required': 'Enter your Name'},
                           max_length=10, min_length=2)
    email = forms.EmailField(
        error_messages={'required': 'Enter your Email'}, max_length=20, min_length=5)
    password = forms.CharField(widget=forms.PasswordInput)
