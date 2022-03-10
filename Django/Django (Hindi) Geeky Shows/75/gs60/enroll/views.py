from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def userProfile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'user': request.user})
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
                    return render(request, 'enroll/profile.html')

        else:
            fm = AuthenticationForm()

        return render(request, 'enroll/login.html', {'form': fm})
    else:
        return redirect('userProfile')


def logoutUser(request):
    logout(request)
    return redirect('userLogin')
