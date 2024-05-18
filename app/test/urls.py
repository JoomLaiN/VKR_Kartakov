from django.urls import path

from test import views

app_name= 'test'

urlpatterns = [
    path('', views.my_test, name='test'),
]
