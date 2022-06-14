"""gs110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.TemplateView.as_view(
    #     template_name="myapp/home.html"), name='home'),

    # path('home/', views.TemplateView.as_view(
    #     template_name="myapp/home.html"), name='home'),

    path('', views.MyView.as_view(), name='home'),

    path('home/', views.MyViewHome.as_view(), name='home'),

    path('excontex/',
         views.MyViewHome.as_view(extra_context={'course': 'Django'}), name='home'),

    path('excontex/<str:course>',
         views.MyViewHome.as_view(), name='home'),



]
