from typing import Mapping
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'title': 'home',
        'content': 'Главная страница моей аптеки'
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('about page')