from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Dipu', help_text='Do this please')
