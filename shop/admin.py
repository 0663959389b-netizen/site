from django.contrib import admin
from .models import Category, Dish, Service, Review, Newsletter, DishRating, Order, ServiceRequest

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number', 'total_price', 'created_at']
    list_filter = ['created_at']

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['phone', 'service_name', 'created_at']
    readonly_fields = ['created_at'] # Щоб не можна було підробити дату заявки

admin.site.register([Category, Service, Review, Newsletter, DishRating])