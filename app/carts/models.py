from django.db import models

from users.models import User
from goods.models import Products

class CartQueryset(models.QuerySet):
    
    def total_price(self):
         return sum(cart.prod_price() for cart in self)
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Клиент')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товары')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'cart'
        verbose_name='Корзина'
        verbose_name_plural = "Корзина"

    objects = CartQueryset().as_manager()

    def prod_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Кол-во {self.quantity}'
        return f'Анонимная корзина | Товар {self.product.name} | Кол-во {self.quantity}'