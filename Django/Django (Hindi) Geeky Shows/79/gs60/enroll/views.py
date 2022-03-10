from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .forms import SignUpForm, EditUserForm, EditAdminForm
from django.contrib import messages
# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/login/')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                group = Group.objects.get(name='Viewer')
                user.groups.add(group)
                messages.success(request, 'Signup Successfully done')

                return redirect('userLogin')

        else:
            fm = SignUpForm()
        return render(request, 'enroll/signup.html', {'form': fm})
    else:
        return redirect('dashboard')


def loginUser(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uName = fm.cleaned_data['username']
                uPass = fm.cleaned_data['password']
                user = authenticate(username=uName, password=uPass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully ')
                    return redirect('dashboard')

        else:
            fm = AuthenticationForm()

        return render(request, 'enroll/login.html', {'form': fm})
    else:
        return redirect('dashboard')


def logoutUser(request):
    logout(request)
    return redirect('userLogin')
