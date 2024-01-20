from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_checkout, name='checkout') 
]
