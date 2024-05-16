
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from orders.models import Order, OrderItem

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Авторизован')
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Аптека - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)
            if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f'{user.username}, Вы зарегистрированы')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Аптека - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Редактирование прошло успешно')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset = OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id")
    )
    
    context = {
        'title': 'Аптека - Профиль',
        'form': form,
        'orders': orders,
        'profile_page': True
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))

def users_cart(request):
    return render(request, 'users/users_cart.html')