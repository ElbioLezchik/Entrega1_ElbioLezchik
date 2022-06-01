from django.contrib import admin

# Register your models here.
from .models import Persona, Mascota, Hobby

admin.site.register(Persona)
admin.site.register(Mascota)
admin.site.register(Hobby)
