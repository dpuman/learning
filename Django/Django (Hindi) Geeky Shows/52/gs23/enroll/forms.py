from django import forms


class StudentRegistration(forms.Form):
    # default
    name = forms.CharField(widget=forms.TextInput)
    # custom
    nameTwo = forms.CharField(widget=forms.Textarea)
    name3 = forms.CharField(widget=forms.CheckboxInput)
    name4 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'newClass', 'id': 'neId'}))
