from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#creamos templates de los formularios
class Productoform(ModelForm):

    class Meta:
        model = Producto
        fields= ['codigo','nombreP','marca','precio','stock','tipo', 'imagen']


class RegistroUsuarioForm(UserCreationForm):
	
    class Meta:
        model = User
        fields = ['username','password1','password2']