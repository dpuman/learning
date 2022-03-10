
from distutils.command.clean import clean
from wsgiref.validate import validator
from django import forms
from django.core import validators


class StudentRegistration(forms.Form):

    def startWithS(value):
        if value[0] != 's':
            raise forms.ValidationError("Staart With S")

    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    nameTwo = forms.CharField(validators=[startWithS])
