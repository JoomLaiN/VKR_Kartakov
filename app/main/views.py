from typing import Mapping
from django.http.response import HttpResponse
from django.shortcuts import render
from goods.models import Products
import random

def index(request):
    products_with_discount = Products.objects.filter(discount__gt=0)
    
    random_products = random.sample(list(products_with_discount), 3)
    #random_products = 0
    context ={
        'title': 'Аптека - Главная',
        'products': random_products,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title': 'Аптека - Отзывы',
        'content': 'О нас',
        'text_on_page': "Тут типа отзывы из views"
    }


    return render(request, 'main/about.html', context)