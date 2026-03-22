from django.shortcuts import render
from .models import Category, Dish, Service  # Імпорт моделей для роботи з базою даних


def home_view(request):
    # Отримуємо категорії (якщо знадобляться для навігації)
    categories = Category.objects.all()

    # Тексти відгуків ПОВНІСТЮ за вашим скриншотом
    reviews = [
        {
            'name': 'Анна та Ігор',
            'text': 'Наш улюблений ресторан! Завжди смачно, затишно і дуже по-домашньому. Level Up Rest стала нашою традицією для сімейних свят. Дякуємо команді за те, що тримаєте таку високу планку якості!'
        },
        {
            'name': 'Марк Сидоренко',
            'text': 'Як поціновувач італійської кухні, я вражений. Паста з морепродуктами — це щось неймовірне, соус просто ідеальний! Видно, що кухарі знають свою справу і вкладають душу в кожну тарілку. Найкраще місце для вишуканої вечері.'
        },
        {
            'name': 'Олена Кравчук',
            'text': 'Неймовірне місце! Level Up Rest — це справжня естетика в кожній деталі. М’яке освітлення створює атмосферу спокою, якої так бракує в місті. Окреме дякую персоналу за професійність та увагу до дрібниць. Обов’язково повернуся ще!'
        }
    ]

    context = {
        'title': 'Головна | Level Up Rest',
        'categories': categories,
        'reviews': reviews,
        # Вступний текст для Hero-блоку
        'welcome_msg': 'Досвід вишуканої кухні у затишній атмосфері. Ласкаво просимо до Level Up Rest, де смак зустрічається з мистецтвом. Насолоджуйтесь вишуканими стравами та відмінним сервісом у розкішному інтер’єрі.'
    }
    return render(request, 'main.html', context)


def menu_view(request):
    # Запит до БД для отримання всіх страв
    dishes = Dish.objects.all()
    context = {
        'title': 'Меню нашого ресторану',
        'dishes': dishes
    }
    return render(request, 'item.html', context)


def services_view(request):
    # Запит до БД для отримання всіх послуг
    services = Service.objects.all()
    context = {
        'title': 'Наші Послуги',
        'services': services
    }
    return render(request, 'services.html', context)


def contacts_view(request):
    # Контактна інформація ресторану
    context = {
        'title': 'Контакти',
        'address': 'м. Луцьк, вул. Лесі Українки, 15',
        'phone': '+38 (050) 123-45-67',
        'email': 'level_up_rest@gmail.com'
    }
    return render(request, 'contacts.html', context)