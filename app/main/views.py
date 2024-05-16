from typing import Mapping
from django.http.response import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    context ={
        'title': 'Аптека - Главная',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title': 'Аптека - Отзывы',
        'content': 'О нас',
        'text_on_page': "Тут типа отзывы из views"
    }


    return render(request, 'main/about.html', context)