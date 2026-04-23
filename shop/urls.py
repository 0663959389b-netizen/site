from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('menu/', views.menu_view, name='menu_url'),
    path('services/', views.services_view, name='services_url'),
    path('contacts/', views.contacts_view, name='contacts_url'),
    path('cart/', views.cart_view, name='cart_url'),
    path('cart/add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:dish_id>/<str:action>/', views.update_cart, name='update_cart'),
]