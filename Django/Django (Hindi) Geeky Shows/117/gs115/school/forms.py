from django import forms

from school.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Your Name'})}
