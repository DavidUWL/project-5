from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_profile, name='view_profile'),


]
