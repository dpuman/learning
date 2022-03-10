
from django import forms


class StudentRegistration(forms.Form):

    name = forms.CharField(max_length=5, min_length=2, strip=False,
                           empty_value='Dipu', error_messages={'required': 'Enter Your Name'})
    roll = forms.IntegerField(min_value=2, max_value=120)
    price = forms.DecimalField(
        min_value=10, max_value=157, max_digits=4, decimal_places=1)
    rate = forms.FloatField(max_value=52, min_value=42)
    agree = forms.BooleanField(label='I agree', label_suffix=' ')
    website = forms.URLField()
    comment = forms.SlugField()
