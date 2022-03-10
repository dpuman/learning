from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .forms import SignUpForm, EditUserForm, EditAdminForm
from django.contrib import messages
# Create your views here.


def userProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser:
                fm = EditAdminForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request, 'successfully Updated')
                return redirect('userProfile')
        else:
            if request.user.is_superuser:
                fm = EditAdminForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'user': request.user, 'form': fm, 'users': users})
    else:
        return HttpResponseRedirect('/login/')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Signup Successfully done')

        else:
            fm = SignUpForm()
        return render(request, 'enroll/signup.html', {'form': fm})
    else:
        return redirect('userProfile')


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
                    return redirect('userProfile')

        else:
            fm = AuthenticationForm()

        return render(request, 'enroll/login.html', {'form': fm})
    else:
        return redirect('userProfile')


def logoutUser(request):
    logout(request)
    return redirect('userLogin')

# with old pass


def changePass(request):
    if request.user.is_authenticated:
        fm = PasswordChangeForm(user=request.user)
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully Changed')
                update_session_auth_hash(request, fm.user)
                return redirect('userProfile')

        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return redirect('userLogin')


# without old pass
def changePass1(request):
    if request.user.is_authenticated:
        fm = SetPasswordForm(user=request.user)
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Successfully Changed')
                update_session_auth_hash(request, fm.user)
                return redirect('userProfile')

        return render(request, 'enroll/changepass1.html', {'form': fm})
    else:
        return redirect('userLogin')


def userDetails(request, id):
    us = User.objects.get(pk=id)
    fm = EditAdminForm(instance=us)
    return render(request, 'enroll/userdetails.html', {'form': fm})
