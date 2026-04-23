from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('menu/', views.menu_view, name='menu_url'),
    path('services/', views.services_view, name='services_url'),
    path('contacts/', views.contacts_view, name='contacts_url'),
]