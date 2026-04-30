from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Dish, Service, Review, DishRating, Order, ServiceRequest, Newsletter
from .forms import RegisterForm, NewsletterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg


def home_view(request):
    subscribed = False

    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email)
            subscribed = True

    reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'main.html', {
        'reviews': reviews,
        'subscribed': subscribed
    })
def menu_view(request):
    if request.method == 'POST' and 'score' in request.POST:
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Тільки для залогінених'}, status=403)
        dish_id = request.POST.get('dish_id')
        score = int(request.POST.get('score'))
        dish = get_object_or_404(Dish, id=dish_id)
        DishRating.objects.update_or_create(dish=dish, user=request.user, defaults={'score': score})
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            new_avg = dish.ratings.aggregate(Avg('score'))['score__avg'] or 0
            return JsonResponse({'new_avg': round(new_avg, 1)})
        return redirect('menu_url')

    cat_id = request.GET.get('category')
    dishes = Dish.objects.filter(category_id=cat_id).annotate(
        avg_rating=Avg('ratings__score')) if cat_id else Dish.objects.annotate(avg_rating=Avg('ratings__score'))
    cart_count = sum(request.session.get('cart', {}).values())
    return render(request, 'item.html',
                  {'categories': Category.objects.all(), 'dishes': dishes, 'cart_count': cart_count})

def add_to_cart(request, dish_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart[str(dish_id)] = cart.get(str(dish_id), 0) + 1
        request.session['cart'] = cart
        request.session.modified = True
        return HttpResponse(status=204)
    return redirect('menu_url')

def cart_view(request):
    cart = request.session.get('cart', {})
    items, total = [], 0
    for d_id, qty in cart.items():
        dish = get_object_or_404(Dish, id=d_id)
        sub = dish.price * qty
        total += sub
        items.append({'dish': dish, 'qty': qty, 'sub': sub})
    return render(request, 'card.html', {'items': items, 'total': total})

def update_cart(request, dish_id, action):
    cart = request.session.get('cart', {})
    did = str(dish_id)
    if did in cart:
        if action == 'increase':
            cart[did] += 1
        elif action == 'decrease':
            if cart[did] > 1:
                cart[did] -= 1
            else:
                del cart[did]
        elif action == 'remove':
            del cart[did]
    request.session['cart'] = cart
    return redirect('cart_url')

def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart: return redirect('menu_url')
    if request.method == 'POST':
        table = request.POST.get('table_number')
        total, items_list = 0, []
        for d_id, qty in cart.items():
            dish = get_object_or_404(Dish, id=d_id)
            total += dish.price * qty
            items_list.append(f"{dish.name} (x{qty})")
        Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            items_json=", ".join(items_list),
            total_price=total,
            table_number=table
        )
        request.session['cart'] = {}
        return render(request, 'thanks.html')
    return render(request, 'checkout_form.html')

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def service_request_view(request):
    if request.method == 'POST':
        s_name = request.POST.get('service_name')
        phone = request.POST.get('phone')
        ServiceRequest.objects.create(service_name=s_name, phone=phone)
        return render(request, 'thanks.html', {'message': 'Ми зателефонуємо вам найближчим часом!'})
    return redirect('services_url')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_url')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def profile_view(request):
    orders = Order.objects.all() if request.user.is_superuser else Order.objects.filter(user=request.user)
    return render(request, 'auth/profile.html', {'orders': orders.order_by('-created_at')})

def contacts_view(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})