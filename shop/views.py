from django.shortcuts import render
from .models import Dish, Service # Імпортуємо моделі, щоб брати дані з бази

def home_view(request):
    context = {
        'title': 'Головна',
        'welcome_msg': 'Вітаємо у Level Up Rest!'
    }
    return render(request, 'main.html', context)

def menu_view(request):
    # Отримуємо всі страви з бази даних
    all_dishes = Dish.objects.all() # Команда: "Дай мені всі записи з таблиці Dish"
    context = {
        'title': 'Меню нашого ресторану',
        'dishes': all_dishes # Передаємо список об'єктів у шаблон
    }
    return render(request, 'item.html', context)

def services_view(request):
    # Отримуємо всі послуги з бази даних
    all_services = Service.objects.all() # Команда: "Дай мені всі записи з таблиці Service"
    context = {
        'title': 'Наші вишукані послуги',
        'services': all_services # Передаємо список послуг у шаблон
    }
    return render(request, 'services.html', context)

def contacts_view(request):
    context = {
        'title': 'Контакти',
        'address': 'м. Луцьк, вул. Лесі Українки, 15',
        'phone': '+38 (050) 123-45-67'
    }
    return render(request, 'contacts.html', context)