from django.shortcuts import render
from .models import Category, Dish, Service, Review


def home_view(request):
    # Тепер відгуки беремо з бази даних, а не пишемо вручну!
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'main.html', {'title': 'Головна - Level Up Rest', 'reviews': reviews})


def menu_view(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        dishes = Dish.objects.filter(category_id=category_id)
    else:
        dishes = Dish.objects.all()

    context = {
        'title': 'Меню ресторану',
        'dishes': dishes,
        'categories': categories
    }
    return render(request, 'item.html', context)


def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'title': 'Наші послуги', 'services': services})
def contacts_view(request):
    return render(request, 'contacts.html', {'title': 'Контакти - Level Up Rest'})