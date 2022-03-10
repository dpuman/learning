
from django import forms


class StudentRegistration(forms.Form):

    name = forms.CharField()

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) < 4:
            raise forms.ValidationError('Not less then 4 char')
        return data
