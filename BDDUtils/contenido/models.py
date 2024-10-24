from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

# Create your models here.
class sesionremota(models.Model):
    class TypePass(models.TextChoices):
        ABODEGA = 'abod', _('abodByC#887-1')
        ACONTABILIDAD = 'acon', _('aconByC#887-1')
        ADIRECTORIO = 'adirector', _('adirByC#887-1')
        AMAQUINARIA = 'amm', _('amaqByC#887-1')
        AOPERACIONES = 'apoer', _('aopeByC#887-1')
        AREMUNERACIONES = 'arem', _('aremByC#887-1')
        ARRHH = 'arhh', _('arrhByC#887-1')
        ATESORERIA = 'ater', _('atesByC#887-1')
        AVENTAS = 'aventas', _('avenByC#887-1')
        BODEGA = 'bod', _('bodeByC#887-1')
        COBRANZA = 'cobranza', _('cobrByC#887-1')
        CONTABILIDAD = 'cont', _('contByC#887-1')
        CONTROLYGESTION = 'ctrl', _('ctrlByC#887-1')
        FINANZA = 'fin', _('finaByC#887-1')
        GERENCIA = 'ger', _('gereByC#887-1')
        INFORMATICA = 'iformat', _('infoByC#887-1')
        PROVEEDORES = 'provedores', _('provByC#887-1')
        RECLUTAMIENTO = 'reclut', _('reclByC#887-1')
        RELACIONADAS = 'relacionadas', _('relaByC#887-1')
        REMUNERACIONES = 'remu', _('remuByC#887-1')
        RRHH = 'rrhh', _('rrhhByC#887-1')
        TESORERIA = 'tesor', _('tesoByC#887-1')
        VENTAS = 'ventas', _('ventByC#887-1')
    
    MY_SISTEMAS = (
        ('AW', 'AW'),
        ('CW', 'CW'),
        ('IW', 'IW'),
        ('NW', 'NW'),
        ('OW', 'OW'),
        ('PW', 'PW'),
        ('SW', 'SW'),
        ('EW', 'EW'),
    )
    
    MY_CERTIDICADOS = (
        ('JB', 'JB'),
        ('OW', 'OW'),
    )
    
    nombre = models.CharField(max_length=50, null=False)
    usuario = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, choices=TypePass, null=False)
    colaborador = models.CharField(max_length=50, null=False, default="DISPONIBLE")
    sistema = MultiSelectField(choices=MY_SISTEMAS, max_choices=3, max_length=30, blank=True, null=True)
    certificados = MultiSelectField(choices=MY_CERTIDICADOS, max_choices=3, max_length=30, blank=True, null=True)
    
    def is_upperclass(self):
        return self.TypePass.ABODEGA
    
    
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
    enlace = models.URLField(max_length=60, null=False)
    usuario = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    
    def url(self):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=self.enlace)
    
    
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