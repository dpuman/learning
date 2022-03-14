from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ContactForm
# Create your views here.


class ClassView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')

################## GET / POST ########################


class MyContact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'myapp/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm()
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse('Succes bor')

############ same View Different Template ###########


def mufunc(request, template):
    msg = 'Hello from view One'
    return render(request, template, {'msg': msg})


class NewClassView(View):
    template = ''

    def get(self, request):
        context = {'msg': 'Hello from Class View'}
        return render(request, self.template, context)
