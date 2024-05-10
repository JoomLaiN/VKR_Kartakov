from typing import Mapping
from django.http.response import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    categories = Categories.objects.all()
    
    context ={
        'title': 'Аптека - Главная',
        'content': 'Главная страница моей аптеки',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title': 'Аптека - Отзывы',
        'content': 'О нас',
        'text_on_page': "Тут типа отзывы из views"
    }


    return render(request, 'main/about.html', context)