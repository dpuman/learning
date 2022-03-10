from django.urls import path
from . import views
urlpatterns = [
    path('course-info/', views.courseInfo, name='courseInfo')
]
