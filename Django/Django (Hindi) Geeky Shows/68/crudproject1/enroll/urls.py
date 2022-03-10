from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.deleteStudent, name='deleteStudent'),
    path('update/<int:id>/', views.updateStudent, name='updateStudent'),
]
