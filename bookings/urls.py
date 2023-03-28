from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/new/', views.booking_new, name='booking_new'),
    path('booking/<int:id>/edit/', views.booking_edit, name='booking_edit'),
    path('booking/<int:id>/delete/', views.booking_delete, name='booking_delete'),
    path('customer/new/', views.customer_new, name='customer_new'),
    path('customer/<int:id>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:id>/delete/', views.customer_delete, name='customer_delete'),
]
