

from django import forms


class StudentRegistration(forms.Form):
    student_id = forms.IntegerField()
    name = forms.CharField(error_messages={'required': 'Enter your Name'},
                           max_length=10, min_length=2)
    email = forms.EmailField(
        error_messages={'required': 'Enter your Email'}, max_length=20, min_length=5)
    password = forms.CharField(widget=forms.PasswordInput)
    comments = forms.CharField(widget=forms.Textarea)
