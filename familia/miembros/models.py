import email
from django.db import models


# Create your models here.
class Mascota(models.Model):
    """Model representa a una mascota."""
    name = models.CharField(max_length=200, help_text='Ingrese el nombre de la mascota')
    tipo_de_mascota = models.CharField(max_length=200, help_text='Ingrese el tipo de mascota. P. ej: Gato, Perro')
    raza = models.CharField(max_length=200, help_text='Ingrese la raza de la mascota')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Hobby(models.Model):
    """Model que representa a un hobby."""
    actividad = models.CharField(max_length=200, help_text='Ingrese el hobby')
    def __str__(self):
        """String for representing the Model object."""
        return self.actividad



class Persona(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email= models.CharField(max_length=100)
    mascota = models.ManyToManyField('Mascota')
    hobby = models.ManyToManyField('Hobby')

    fecha_de_fallecimiento = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['apellido', 'nombre']


