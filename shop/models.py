from django.db import models

# Таблиця 1: Категорії страв (наприклад: Салати, Супи)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії") # Текстове поле для назви

    def __str__(self):
        return self.name # Показуємо назву категорії в списку

# Таблиця 2: Страви (Об'єднана з Категорією через ForeignKey)
class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія") # Зв'язок з першою таблицею
    name = models.CharField(max_length=100, verbose_name="Назва страви") # Назва страви
    description = models.TextField(verbose_name="Склад/Опис", blank=True) # Опис (може бути пустим)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна") # Ціна з двома знаками після коми

    # Поля для дати (вимога лаби)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о") # Фіксується при створенні
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о") # Оновлюється при кожній зміні

    def __str__(self):
        return self.name

# Таблиця 3: Послуги ресторану
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Послуга") # Назва послуги
    details = models.TextField(verbose_name="Деталі послуги") # Опис того, що входить у послугу

    def __str__(self):
        return self.title