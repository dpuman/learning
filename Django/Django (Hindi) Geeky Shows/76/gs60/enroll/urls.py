from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='sugnup'),
    path('login/', views.loginUser, name='userLogin'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('profile/', views.userProfile, name='userProfile'),
    path('change-pass/', views.changePass, name='changePass'),
    path('change-pass1/', views.changePass1, name='changePass1'),
]
