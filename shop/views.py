from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Dish, Service, Review, DishRating
from .forms import NewsletterForm
from django.http import HttpResponse
from django.db.models import Avg

def home_view(request):
    subscribed = False
    error_message = None
    news_form = NewsletterForm()

    if request.method == 'POST' and 'email' in request.POST:
        email = request.POST.get('email')
        from .models import Newsletter

        if Newsletter.objects.filter(email=email).exists():
            subscribed = True
        else:
            news_form = NewsletterForm(request.POST)
            if news_form.is_valid():
                news_form.save()
                subscribed = True
            else:
                error_message = "❌ Ой! Введіть, будь ласка, коректну адресу електронної пошти."

    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'main.html', {
        'title': 'Головна - Level Up Rest',
        'reviews': reviews,
        'news_form': news_form,
        'subscribed': subscribed,
        'error_message': error_message
    })

def menu_view(request):
    if request.method == 'POST' and 'score' in request.POST:
        dish_id = request.POST.get('dish_id')
        score = request.POST.get('score')

        if dish_id and score:
            dish = get_object_or_404(Dish, id=dish_id)
            user_ratings = request.session.get('user_ratings', {})

            if dish_id in user_ratings:
                try:
                    rating = DishRating.objects.get(id=user_ratings[dish_id])
                    rating.score = score
                    rating.save()
                except DishRating.DoesNotExist:
                    new_rating = DishRating.objects.create(dish=dish, score=score)
                    user_ratings[dish_id] = new_rating.id
            else:
                new_rating = DishRating.objects.create(dish=dish, score=score)
                user_ratings[dish_id] = new_rating.id

            request.session['user_ratings'] = user_ratings
            request.session.modified = True

        return redirect('menu_url')

    category_id = request.GET.get('category')
    if category_id:
        dishes = Dish.objects.filter(category_id=category_id).annotate(avg_rating=Avg('ratings__score'))
    else:
        dishes = Dish.objects.annotate(avg_rating=Avg('ratings__score'))

    categories = Category.objects.all()
    cart_count = sum(request.session.get('cart', {}).values())

    return render(request, 'item.html', {
        'title': 'Меню - Level Up Rest',
        'categories': categories,
        'dishes': dishes,
        'cart_count': cart_count
    })

def add_to_cart(request, dish_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        dish_id_str = str(dish_id)
        if dish_id_str in cart:
            cart[dish_id_str] += 1
        else:
            cart[dish_id_str] = 1
        request.session['cart'] = cart
        request.session.modified = True

        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'fetch' in request.path:
            return HttpResponse(status=204)  # Повертаємо порожню відповідь для JS

    return redirect('menu_url')

def update_cart(request, dish_id, action):
    cart = request.session.get('cart', {})
    dish_id_str = str(dish_id)
    if dish_id_str in cart:
        if action == 'increase':
            cart[dish_id_str] += 1
        elif action == 'decrease':
            if cart[dish_id_str] > 1:
                cart[dish_id_str] -= 1
            else:
                del cart[dish_id_str]
        elif action == 'remove':
            del cart[dish_id_str]
    request.session['cart'] = cart
    return redirect('cart_url')

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    dishes = Dish.objects.filter(id__in=cart.keys())

    for dish in dishes:
        quantity = cart[str(dish.id)]
        subtotal = dish.price * quantity
        total += subtotal
        items.append({
            'dish': dish,
            'qty': quantity,
            'sub': subtotal
        })

    return render(request, 'card.html', {
        'title': 'Ваш кошик - Level Up Rest',
        'items': items,
        'total': total
    })


def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'title': 'Наші послуги', 'services': services})


def contacts_view(request):
    return render(request, 'contacts.html', {'title': 'Контакти - Level Up Rest'})