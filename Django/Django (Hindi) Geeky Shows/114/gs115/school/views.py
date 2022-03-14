import imp
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class ContactView(FormView):
    template_name = 'school/contactform.html'
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name': 'Dipu'}

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'school/thankyou.html'
