from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  #Esta es la primer view
    path('agregar_mascota/', views.agregar_mascota, name="agregar_mascota"),
    path('agregar_persona/', views.agregar_persona, name="agregar_persona"),
    path('agregar_hobby/', views.agregar_hobby, name="agregar_hobby"),
    path('buscar_mascota/', views.buscar_mascota, name="buscar_mascota"),
    path('buscar_persona/', views.buscar_persona, name="buscar_persona"),
    path('buscar_hobby/', views.buscar_hobby, name="buscar_hobby"),
]