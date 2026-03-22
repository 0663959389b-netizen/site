from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('services/', views.services_view, name='services'),
    path('contacts/', views.contacts_view, name='contacts'),
]