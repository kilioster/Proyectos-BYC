from django.db import models

class Casa(models.Model):
    direccion = models.CharField(max_length=30, blank=False, null=False, default='Ejemplo')
    baths = models.IntegerField(null=False, blank=False, default='1')
    rooms = models.IntegerField(null=False, blank=False, default='1')
    description = models.CharField(max_length=100, blank=False, null=False, default='Ejemplo0')
    contacto = models.CharField(max_length=100, blank=False, null=False, default='www.whatsapp.com')
    imagen = models.ImageField(default='../static/media/casa.webp', blank=True)
    
    def __str__(self):
        return self.direccion
    
class Photos(models.Model):
    project = models.ForeignKey(Casa, on_delete=models.SET_NULL, null=True, blank=True)
    gallery = models.FileField(upload_to='images/')
    
    def __str__(self):
        return self.project.direccion