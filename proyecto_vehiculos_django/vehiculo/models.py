from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser, Permission, ContentType

# Create your models here.


class Vehiculo(models.Model):
    MARCA_CHOICES = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    CATEGORIA_CHOICES = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def obtener_categoria_precio(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'

    def __str__(self):
        return self.modelo

"""
Lo comente porque se utilizo una vez y para generar permisos, hubiece sido mejor generarlo de consola.
# Permiso para visualizar el catálogo de vehículos
visualizar_catalogo_permission = Permission.objects.create(
    codename='visualizar_catalogo',
    name='Puede visualizar Catálogo de Vehículos',
    content_type=ContentType.objects.get_for_model(Vehiculo),
)

# Permiso para agregar un vehículo
add_vehiculomodel_permission = Permission.objects.create(
    codename='add_vehiculomodel',
    name='Puede agregar Vehículo',
    content_type=ContentType.objects.get_for_model(Vehiculo),
)
"""
