from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.utils import q_search

from goods.models import Products, Categories

# Create your views here.
def catalog(request, category_slug=None):
    
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        try:
            categories = Categories.objects.get(slug=category_slug)
            goods = Products.objects.filter(category=categories)
        except Categories.DoesNotExist:
            goods = []  # Если категория не существует, возвращаем пустой список
        
    if on_sale:
        goods = [good for good in goods if good.discount > 0]
    if order_by and order_by != 'default':
        if order_by == 'price':
            goods = sorted(goods, key=lambda x: x.sell_price())
        elif order_by == '-price':
            goods = sorted(goods, key=lambda x: x.sell_price(), reverse=True)
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    
    context = {
        'title': 'Аптека - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
        'on_sale': on_sale,
        'order_by': order_by,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    
    context = {
        'product':product,
        'profile_page': True
    }

    return render(request, 'goods/product.html', context=context)