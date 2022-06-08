from django import forms

class MascotaForm(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=200)
    tipo_de_mascota = forms.CharField(max_length=200)
    raza = forms.CharField(max_length=200)

class HobbyForm(forms.Form):
    #Especificar los campos
    actividad = forms.CharField(max_length=200)

class PersonaForm(forms.Form):
    #Especificar los campos
    apellido = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    fecha_de_nacimiento = forms.DateField(label="fecha_de_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(label="Número")
    correo_electronico = forms.EmailField(label="Email")
    fecha_de_fallecimiento = forms.DateField(label="fecha_de_fallecimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))

class BuscarMascotaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarPersonaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class BuscarHobbyForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")