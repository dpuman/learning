from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(label="My Name", label_suffix=" :", initial='Dipu')
    email = forms.EmailField(initial="Dipu@mail.com")
