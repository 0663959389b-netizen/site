from django.shortcuts import render

# Create your views here.

from django.shortcuts import render # Імпортуємо функцію для відображення HTML

def home_view(request): # Функція для головної сторінки
    context = { # Дані для шаблону (контекст)
        'title': 'Головна',
        'welcome_msg': 'Вітаємо у нашому ресторані!'
    }
    return render(request, 'main.html', context) # Рендеримо головну сторінку

def menu_view(request): # Функція для сторінки меню
    context = {
        'title': 'Меню',
        'dishes': ['Борщ', 'Вареники', 'Узвар'] # Список страв передаємо через контекст
    }
    return render(request, 'item.html', context) # Рендеримо сторінку з меню