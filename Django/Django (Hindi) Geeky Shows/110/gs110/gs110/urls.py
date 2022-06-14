
from re import template
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(
        template_name='myapp/home.html'), name='home'),

    path('home/', views.RedirectView.as_view(url='/'), name='newHome'),
    path('info/', views.RedirectView.as_view(url='/'), name='info'),

    path('facebook/', views.RedirectView.as_view(url='http://www.facebook.com'), name='fb'),
    path('you/', views.MyYoutubeReddirect.as_view(), name='ytube'),

    path('me/', views.RedirectView.as_view(pattern_name='newHome'), name='me'),

    path('info/<slug:info>',
         views.TemplateView.as_view(template_name='myapp/home.html'), name='newInfo'),
    path('me/<slug:info>', views.MyRedirectView.as_view(), name='meSlug'),





]
