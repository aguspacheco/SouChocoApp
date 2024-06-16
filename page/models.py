from django.db import models

class Producto(models.Model):
    nombre = models.CharField(null=False, max_length=100)
    descripcion = models.CharField(null=False, max_length=500)
    categoria = models.CharField(null=False,max_length=500)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
