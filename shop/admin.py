from django.contrib import admin
from .models import Category, Dish, Service, Review

# Твої круті налаштування для відображення страв
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']

# Реєстрація інших таблиць
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Review)