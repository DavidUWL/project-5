from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('order_history/<order_number>',
         views.purchase_history,
         name='purchase_history'
         ),


]
