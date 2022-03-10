from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='sugnup'),
    path('login/', views.loginUser, name='userLogin'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('dashboard/', views.dashboard, name='dashboard'),

]