from django.contrib import admin
from .models import Category, Dish, Service # Імпортуємо наші моделі

# Налаштовуємо адмінку для страв
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    # Відображаємо назву, ціну та дати, як просить викладач
    list_display = ('name', 'category', 'price', 'created_at', 'updated_at')
    # Додаємо фільтр за категорією та датою створення
    list_filter = ('category', 'created_at')
    # Додаємо пошук за назвою страви
    search_fields = ('name',)

# Реєструємо інші моделі просто (без додаткових налаштувань)
admin.site.register(Category)
admin.site.register(Service)