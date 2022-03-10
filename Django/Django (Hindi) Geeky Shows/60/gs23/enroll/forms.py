
from distutils.command.clean import clean
from django import forms


class StudentRegistration(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        valueName = self.cleaned_data['name']
        valueEmail = self.cleaned_data['email']

        if len(valueName) < 4:
            raise forms.ValidationError('4')

        if len(valueEmail) < 10:
            raise forms.ValidationError('10')
