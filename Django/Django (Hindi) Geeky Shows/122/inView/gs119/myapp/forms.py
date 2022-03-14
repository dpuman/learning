from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext, gettext_lazy as _


class MyLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'my-class'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'my-class'}),
    )
