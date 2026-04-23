from django.contrib import admin
from .models import Category, Dish, Service, Review, Newsletter, DishRating

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin): list_display = ['name', 'price', 'category']
admin.site.register([Category, Service, Review, Newsletter, DishRating])