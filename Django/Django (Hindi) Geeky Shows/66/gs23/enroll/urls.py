from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, {'check': 'Ok'}, name="home"),
    # path('<my_id>/', views.show,  name="show"),
    path('<int:my_id>/', views.show,  name="show"),
    path('<int:my_id>/<int:info>/', views.showDetails,  name="showDetails"),

]
