from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from django.views.generic import TemplateView


class Profile(TemplateView):
    template_name = "registration/profile.html"


class About(TemplateView):
    template_name = 'registration/about.html'
