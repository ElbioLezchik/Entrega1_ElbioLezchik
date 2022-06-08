from curses.ascii import HT
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from miembros.forms import BuscarMascotaForm, BuscarPersonaForm, BuscarHobbyForm, MascotaForm, PersonaForm, HobbyForm
from miembros.models import Mascota, Hobby, Persona

# Create your views here.
def index(request):
    return render(request, "miembros/index.html")

def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            tipo_de_mascota = form.cleaned_data['tipo_de_mascota']
            raza = form.cleaned_data['raza']
            Mascota(nombre=nombre, tipo_de_mascota=tipo_de_mascota, raza=raza).save()
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'miembros/form_carga_mascota.html', {'form': form})


def agregar_persona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            fecha_de_nacimiento = form.cleaned_data['fecha_de_nacimiento']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            correo_electronico = form.cleaned_data['email']
            fecha_de_fallecimiento = form.cleaned_data['fecha_de_fallecimiento']
            Persona(nombre=nombre, apellido=apellido, fecha_de_nacimiento=fecha_de_nacimiento, direccion=direccion, telefono=telefono, correo_electronico=correo_electronico, fecha_de_fallecimiento=fecha_de_fallecimiento).save()
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'miembros/form_carga_persona.html', {'form': form})


def agregar_hobby(request):
    if request.method == "POST":
        form = HobbyForm(request.POST)
        if form.is_valid():
            actividad = form.cleaned_data['actividad']
            Hobby(actividad=actividad).save()
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = HobbyForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    return render(request, 'miembros/form_carga_hobby.html', {'form': form})


def buscar_mascota(request):
    if request.method == "GET":
        form_busqueda_mascota = BuscarMascotaForm()
        return render(request, 'miembros/form_busqueda_mascota.html', {"form_busqueda_mascota": form_busqueda_mascota})
    elif request.method == "POST":
        form_busqueda_mascota = BuscarMascotaForm(request.POST)
        if form_busqueda_mascota.is_valid():
            palabra_a_buscar = form_busqueda_mascota.cleaned_data['palabra_a_buscar']
            mascotas = Mascota.objects.filter(nombre__icontains=palabra_a_buscar)
    return  render(request, 'miembros/lista_mascotas.html', {"mascotas": mascotas})

def buscar_persona(request):
    if request.method == "GET":
        form_busqueda_persona = BuscarPersonaForm()
        return render(request, 'miembros/form_busqueda_persona.html', {"form_busqueda_persona": form_busqueda_persona})
    elif request.method == "POST":
        form_busqueda_persona = BuscarPersonaForm(request.POST)
        if form_busqueda_persona.is_valid():
            palabra_a_buscar = form_busqueda_persona.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)
    return  render(request, 'miembros/lista_personas.html', {"personas": personas})

def buscar_hobby(request):
    if request.method == "GET":
        form_busqueda_hobby = BuscarHobbyForm()
        return render(request, 'miembros/form_busqueda_hobby.html', {"form_busqueda_hobby": form_busqueda_hobby})
    elif request.method == "POST":
        form_busqueda_hobby = BuscarHobbyForm(request.POST)
        if form_busqueda_hobby.is_valid():
            palabra_a_buscar = form_busqueda_hobby.cleaned_data['palabra_a_buscar']
            hobbys = Hobby.objects.filter(actividad__icontains=palabra_a_buscar)
    return  render(request, 'miembros/lista_hobbys.html', {"hobbys": hobbys})
