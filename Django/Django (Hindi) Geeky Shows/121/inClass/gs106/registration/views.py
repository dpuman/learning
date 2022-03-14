import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator


class Profile(TemplateView):
    template_name = "registration/profile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class About(TemplateView):
    template_name = 'registration/about.html'

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
