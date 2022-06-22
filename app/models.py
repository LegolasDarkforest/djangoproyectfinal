from tkinter import CASCADE
from django.db import models

# Create your models here.
#ultimos cambios se agregaron las clases meta a todos las tablas 
# y se borro la fecha anterior que se colocaba manual por una que se coloca sola segun la fecha actual
class TipoProducto (models.Model):
    tipo =  models.CharField(max_length=30)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'db_tipo_producto'

class Producto (models.Model):
    codigo =  models.IntegerField(null=False,primary_key=True)
    nombreP =  models.CharField(max_length=30)
    marca =  models.CharField(max_length=30)
    precio =  models.IntegerField()
    stock = models.IntegerField()
    tipo =  models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
   

    def __str__(self):
        return self.nombreP
    
    class Meta:
        db_table = 'db_producto'

class TipoUsuario (models.Model):
    tipoUser = models.CharField(max_length=15)

    def __str__(self):
        return self.tipoUser
    
    class Meta:
        db_table = 'db_tipo_usuario'

class Usuario (models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    tipo = models.ForeignKey(TipoUsuario, on_delete= models.CASCADE)
    imagen_perfil = models.ImageField(upload_to="perfil", null=True)

    def __str__(self):
        return self.rut
    
    class Meta:
        db_table = 'db_usuario'

class Carrito (models.Model):
    codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        db_table= 'db_Carrito'