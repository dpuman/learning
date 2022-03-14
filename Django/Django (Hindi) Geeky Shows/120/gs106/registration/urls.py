from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.Profile.as_view(), name='profile'),
    path('', views.about, name='about')
]
