from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    groups = models.ManyToManyField(Group, related_name='user_manage')
    user_permissions = models.ManyToManyField(Permission, related_name='user_manage')
    def __str__(self):
        return self.email

class Categoria(models.Model):
    codigo_categoria = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Edición' )

    def _str_(self):
        return self.categoria

class Producto(models.Model):
    codigo_Producto = models.CharField(max_length=100)
    codigo_categoria = models.ForeignKey(Categoria,verbose_name = 'Categoria', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Edición' )

    def _str_(self):
        return self.nombre

class Cliente(models.Model):
    codigo_cliente = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Edición' )

    def _str_(self):
        return f"{self.nombres} {self.apellidos}"

class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Edición' )

    def _str_(self):
        return f"{self.idPedido} - {self.cliente} - {self.producto}"

class Pago(models.Model):
    Pago = models.CharField(max_length=100)
    fecha_pago = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Edición' )

    def _str_(self):
        return f"{self.idPago} - {self.pedido}"

class Envio(models.Model):
    Envio = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    fecha_entrega = models.DateField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 
    updated = models.DateTimeField(auto_now = True, verbose_name='Fecha de Edición' )

    def _str_(self):
        return f"{self.idEnvio} - {self.pedido}"