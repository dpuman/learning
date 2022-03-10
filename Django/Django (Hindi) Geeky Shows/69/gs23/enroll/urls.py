from django.urls import path, register_converter
from . import views, converters
register_converter(converters.FourDigitYearConverter, 'yyyy')
urlpatterns = [

    path('', views.show,  name="show"),


]
