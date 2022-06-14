from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import MyLoginForm
urlpatterns = [
    path('', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='myapp/dashboard.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html',
         authentication_form=MyLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),

    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='myapp/changepassword.html', success_url='/change-password-done/'), name='passwordChange'),

    path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='myapp/changepassworddone.html'), name='passwordChangeDone'),

]
