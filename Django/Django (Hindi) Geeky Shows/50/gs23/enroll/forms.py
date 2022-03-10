from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    key = forms.IntegerField(widget=forms.HiddenInput())
