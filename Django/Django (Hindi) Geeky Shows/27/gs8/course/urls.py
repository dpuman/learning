from django.urls import path
from . import views
urlpatterns = [
    path('my-course/', views.myCourse),
]
