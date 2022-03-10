
from distutils.command.clean import clean
# from wsgiref.validate import validator
from django import forms
# from django.core import validators


class StudentRegistration(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(
        widget=forms.PasswordInput, label='Password(again)')

    def clean(self):
        clean_data = super().clean()
        passOne = self.cleaned_data['password']
        passTwo = self.cleaned_data['repassword']

        if passTwo != passOne:
            raise forms.ValidationError('Pass dose not matched')
