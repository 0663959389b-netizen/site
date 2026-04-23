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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Послуга")
    details = models.TextField(verbose_name="Деталі послуги")
    image = models.ImageField(upload_to='services/', verbose_name="Фото послуги", blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user_name = models.CharField(max_length=100, verbose_name="Ім'я гостя")
    text = models.TextField(verbose_name="Відгук")
    rating = models.IntegerField(default=5, verbose_name="Оцінка (від 1 до 5)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name