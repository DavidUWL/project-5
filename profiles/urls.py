from django.urls import path, include
from . import views
from .views import delete_user_profile, delete_user_rating

urlpatterns = [
    path('',
         views.view_profile,
         name='view_profile'
         ),
    path(
        'order_history/<order_number>',
        views.purchase_history,
        name='purchase_history'
    ),
    path(
        '',
        views.delete_user_profile,
        name='delete_user_profile'
    ),
    path(
        'delete_user_rating/<int:rating_id>/',
        views.delete_user_rating,
        name='delete_user_rating'
    )
]
