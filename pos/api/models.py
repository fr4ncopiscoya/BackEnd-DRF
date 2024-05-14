from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = CloudinaryField('image', default='')
    Categoria = models.ForeignKey(Categoria, related_name='Productos', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=200)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre