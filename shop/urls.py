from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomSetPasswordForm

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('menu/', views.menu_view, name='menu_url'),
    path('services/', views.services_view, name='services_url'),
    path('service-request/', views.service_request_view, name='service_request'),
    path('contacts/', views.contacts_view, name='contacts_url'),

    path('cart/', views.cart_view, name='cart_url'),
    path('cart/add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:dish_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout_view, name='checkout_url'),

    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home_url'), name='logout'),
    path('profile/', views.profile_view, name='profile_url'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auth/password_reset.html',
             success_url=reverse_lazy('password_reset_done')
         ), name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auth/password_reset_done.html'
         ), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auth/password_reset_confirm.html',
             success_url=reverse_lazy('password_reset_complete')
         ), name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_complete.html'
         ), name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(
         template_name='auth/password_reset_confirm.html',
         form_class=CustomSetPasswordForm,
         success_url=reverse_lazy('password_reset_complete')
     ), name='password_reset_confirm'),
]