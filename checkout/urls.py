from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success')
]
