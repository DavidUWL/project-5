from django.urls import path, include
from . import views
from .views import delete_user_profile

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path(
        'order_history/<order_number>',
         views.purchase_history,
         name='purchase_history'
        ),
    path(
        '', 
        delete_user_profile, 
        name='delete_user_profile'
        )


]
