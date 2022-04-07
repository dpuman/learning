
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students', views.students),
    path('api/<int:id>', views.student_details),
]
