
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete/<int:pk>/', views.DeleteStudent.as_view(), name='delete'),
    path('thankyou/', views.SuccessView.as_view(), name='thankyou'),

]
