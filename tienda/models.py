from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    SEXO=(('F','Femenino'),('M','Masculino'))#Arreglo
    sexo = models.CharField(max_length=1,choices=SEXO,default='M')
    S = 'S'
    TALLA_CHOICES=(
        ('S','CHICA'),
        ('M','MEDIANA'),
        ('L','GRANDE')
    )
    talla = models.CharField(max_length=30,choices=TALLA_CHOICES,default=S)
    foto = models.URLField(default="")
    costo = models.CharField(max_length=50,default="")

    def NombreProducto(self):
        cadena = '{0} {1}'
        return cadena.format(self.nombre, self.talla)

    def __str__(self):
        return self.NombreProducto()

class Clientes(models.Model):
    Nombre=models.CharField(max_length=20)
    Telefono=models.CharField(max_length=10)
    Email= models.EmailField()
    Domicilio=models.TextField()

    def NombreCompleto(self):
        cadena = '{0} {1}'
        return cadena.format(self.Nombre, self.Email)

    def __str__(self):
        return self.NombreCompleto()
