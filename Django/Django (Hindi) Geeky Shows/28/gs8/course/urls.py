from django.urls import path
from . import views
urlpatterns = [
    path('my-course/', views.myCourse),
    path('filters/', views.myFilter),
    path('tag-filter/', views.myTagFilter),
]
