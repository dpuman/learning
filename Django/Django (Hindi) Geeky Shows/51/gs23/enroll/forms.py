from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(label="My Name", label_suffix=" :",
                           initial='Dipu', help_text='write your name')
    email = forms.EmailField(initial="Dipu@mail.com")
