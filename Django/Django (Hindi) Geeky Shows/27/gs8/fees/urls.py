from django.urls import path
from . import views
urlpatterns = [
    path('my-fees', views.myFees)
]
