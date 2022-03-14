from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('profile/', login_required(views.Profile.as_view()), name='profile'),
    path('', staff_member_required(views.About.as_view()), name='about')
]
