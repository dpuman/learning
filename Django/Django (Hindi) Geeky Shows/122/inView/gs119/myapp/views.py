from django.shortcuts import render
from .forms import MyLoginForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
# Create your views here.


class MyLoginView(LoginView):
    template_name = 'myapp/login.html'
    authentication_form = MyLoginForm


class MyLogoutView(LogoutView):
    template_name = 'myapp/logout.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'myapp/changepassword.html'
    success_url = '/change-password-done/'


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'myapp/changepassworddone.html'
