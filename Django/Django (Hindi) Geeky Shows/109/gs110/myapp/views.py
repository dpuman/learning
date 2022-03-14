from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class MyView(TemplateView):
    template_name = 'myapp/home.html'


class MyViewHome(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {
        #     'name': 'Dipu',
        #     'roll': 102
        # }

        # for extra context/kwargs
        context['name'] = "Dipu"
        context['roll'] = 102
        # for Dynamic url argument value
        print(kwargs)
        return context
