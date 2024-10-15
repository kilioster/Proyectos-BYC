from django.db import models

# Create your models here.
class sesionremota(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    usuario = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    colaborador = models.CharField(max_length=50, null=False)
    sistema = models.CharField(max_length=20,null=True)
    certificados = models.CharField(max_length=20, null=True)
    
    
    def __str__(self):
        return self.nombre
    
class nubecorporativa(models.Model):
    cuenta = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=30, null=False)
    departamentos = models.CharField(max_length=50, null=False)
    
    
    def __str__(self):
        return self.cuenta
    
class cuentas(models.Model):
    plataforma = models.CharField(max_length=30, null=False)
    cuenta = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.plataforma
    
class dominios(models.Model):
    dominio = models.CharField(max_length=50, null=False)
    enlace = models.CharField(max_length=60, null=False)
    usuario = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.dominio
    
class cuentas_admin(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    correo = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=30, null=False)
    tipo_cargo = models.CharField(max_length=30, default="Administrativo")
    cargo = models.CharField(max_length=30, null=True)
    passzoho = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.nombre
    
class cuentas_ope(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    correo = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=30, null=False)
    tipo_cargo = models.CharField(max_length=30, default="Operador")
    cargo = models.CharField(max_length=30, null=True)
    passzoho = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.nombre
    
class direccionamiento(models.Model):
    ip = models.CharField(max_length=15, null=False)
    nombre_dispositivo = models.CharField(max_length=50, null=True, default="Dispositivo no registrado")
    descripcion = models.CharField(max_length=100, null=True)
    mac = models.CharField(max_length=17, null=True)
    
    def __str__(self):
        return self.ip