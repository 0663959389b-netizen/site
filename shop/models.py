from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    name = models.CharField(max_length=100, verbose_name="Назва страви")
    description = models.TextField(verbose_name="Склад/Опис", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    image = models.ImageField(upload_to='dishes/', verbose_name="Фото страви", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name


# Таблиця 3: Послуги ресторану (ТАКОЖ ДОДАЄМО ФОТО)
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Послуга")
    details = models.TextField(verbose_name="Деталі послуги")

    # --- ДОДАЙ ЦЕЙ РЯДОК ---
    image = models.ImageField(upload_to='services/', verbose_name="Фото послуги", blank=True, null=True)

    def __str__(self):
        return self.title