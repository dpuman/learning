
from django.contrib import admin
from django.urls import path, include
from api import views
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    path('auth/', include('rest_framework.urls', namespace='auth')),
]
