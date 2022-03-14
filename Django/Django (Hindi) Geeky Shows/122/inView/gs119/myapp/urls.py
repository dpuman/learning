from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import MyLoginForm
urlpatterns = [
    path('', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='myapp/dashboard.html'), name='home'),

    path('login/', views.MyLoginView.as_view(), name='login'),

    path('logout/', views.MyLogoutView.as_view(), name='logout'),

    path('change-password/', views.MyPasswordChangeView.as_view(),
         name='passwordChange'),

    path('change-password-done/', views.MyPasswordChangeDoneView.as_view(),
         name='passwordChangeDone'),

]
