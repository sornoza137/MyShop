from django.urls import path
from .import views
from .views import home, categoria_celulares, categoria_monitores, categoria_muebles, carrito, cuenta


urlpatterns = [
    #path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),
     path('categorias/celulares/', categoria_celulares, name='categoria_celulares'),
    path('categorias/monitores/', categoria_monitores, name='categoria_monitores'),
    path('categorias/muebles/', categoria_muebles, name='categoria_muebles'),
     path('carrito/', carrito, name='carrito'),
     path('cuenta/', cuenta, name='cuenta'),
]