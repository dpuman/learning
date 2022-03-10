from dataclasses import field
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='password(again)',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {'email': 'Email'}


class EditUserForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'date_joined']
        labels = {'email': 'Email'}
