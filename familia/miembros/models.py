
from django.db import models


# Create your models here.
class Mascota(models.Model):
    """Model representa a una mascota."""
    nombre = models.CharField(max_length=200, help_text='Ingrese el nombre de la mascota')
    tipo_de_mascota = models.CharField(max_length=200, help_text='Ingrese el tipo de mascota. P. ej: Gato, Perro')
    raza = models.CharField(max_length=200, help_text='Ingrese la raza de la mascota')

    def __str__(self):
        
        return self.nombre


class Hobby(models.Model):
    
    actividad = models.CharField(max_length=200, help_text='Ingrese el hobby')
    
    def __str__(self):
    
        return self.actividad



class Persona(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    mascota = models.ManyToManyField(Mascota, null=True, blank=True, help_text='Seleccione la mascota de este familiar')
    hobby = models.ManyToManyField(Hobby, null=True, blank=True, help_text='Seleccione el hobby de este familiar')
    fecha_de_fallecimiento = models.DateField(null=True, blank=True)

    

    def __str__(self):
        
        return f'{self.apellido}, {self.nombre}'


