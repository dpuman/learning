from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Signup Successfully done')

    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})
