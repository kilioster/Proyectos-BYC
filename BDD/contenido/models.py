from django.db import models

# Create your models here.
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
    
    nombre = models.CharField(max_length=50, null=True)
    usuario = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, choices=TypePass, null=True)
    colaborador = models.CharField(max_length=50, null=True, default="DISPONIBLE")
    sistema = MultiSelectField(choices=MY_SISTEMAS, max_choices=8, max_length=30, blank=True, null=True)
    certificados = MultiSelectField(choices=MY_CERTIDICADOS, max_choices=3, max_length=30, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Sesion Remota'
        verbose_name_plural = 'Sesiones Remotas'
    
    def is_upperclass(self):
        return self.TypePass.ABODEGA
    
    
    def __str__(self):
        return self.nombre
    
class nubecorporativa(models.Model):
    cuenta = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=30, null=True)
    departamentos = models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name = 'Nube Corporativa'
        verbose_name_plural = 'Nubes Corporativas'
    
    def __str__(self):
        return self.cuenta
    
class cuentas(models.Model):
    plataforma = models.CharField(max_length=30, null=True)
    cuenta = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    
    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
    
    def __str__(self):
        return self.plataforma
    
class dominios(models.Model):
    dominio = models.CharField(max_length=50, null=True, verbose_name='DOMINION')
    enlace = models.URLField(max_length=60, null=True, verbose_name='ENLACE')
    usuario = models.CharField(max_length=30, null=True, verbose_name='USUARIO')
    password = models.CharField(max_length=30, null=True, verbose_name='PASSWORD')
    
    class Meta:
        verbose_name = 'Dominio'
        verbose_name_plural = 'Dominios'
    
    def url(self):
        return format_html(
            '<a href="{url}">{url}</a>',
            self.enlace,
        )
    
class cuentas_admin(models.Model):
    nombre = models.CharField(max_length=40, null=True)
    correo = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=30, null=True)
    tipo_cargo = models.CharField(max_length=30, default="Administrativo")
    cargo = models.CharField(max_length=30, null=True)
    passzoho = models.CharField(max_length=30, null=True)
    
    class Meta:
        verbose_name = 'Cuenta Admin'
        verbose_name_plural = 'Cuentas Admins'
    
    def __str__(self):
        return self.nombre
    
class cuentas_ope(models.Model):
    nombre = models.CharField(max_length=40, null=True)
    correo = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=30, null=True)
    tipo_cargo = models.CharField(max_length=30, default="Operador")
    cargo = models.CharField(max_length=30, null=True)
    passzoho = models.CharField(max_length=30, null=True)
    
    class Meta:
        verbose_name = 'Cuenta Operador'
        verbose_name_plural = 'Cuentas Operadores'
    
    def __str__(self):
        return self.nombre
    
class direccionamiento(models.Model):
    ip = models.CharField(max_length=15, null=True)
    nombre_dispositivo = models.CharField(max_length=50, null=True, default="Dispositivo no registrado")
    descripcion = models.CharField(max_length=100, null=True)
    mac = models.CharField(max_length=17, null=True)
    
    class Meta:
        verbose_name = 'Direccionamiento'
        verbose_name_plural = 'Direccionamientos'
    
    def __str__(self):
        return self.ip
    
class inventario(models.Model):
    
    class Typeempresa(models.TextChoices):
        GBYC = 'GBYC', _('GBYC')
        BYCT = 'BYCT', _('BYCT')
        BULL = 'BULL', _('BULL')
        IVIC = 'IVIC', _('IVIC')
        FEMM = 'FEMM', _('FEMM')
        KCBS = 'KCBS', _('KCBS')
        
    class Typearea(models.TextChoices):
        BODEGA = 'Bodega', _('Bodega')
        CONTABILIDAD = 'Contabilidad', _('Contabilidad')
        CONTROLYGESTION = 'Control y Gestion', _('Gestion y Gestion')
        DESARROLLO = 'Desarrollo', _('Desarrollo')
        GERENCIA = 'Gerencia', _('Gerencia')
        INSPECTOREQUIPO = 'Inspector de Equipos', _('Inspector de Equipos')
        MAQUINARIA = 'Maquinarias', _('Maquinarias')
        OPERACIONES = 'Operaciones', _('Operaciones')
        PREVENCION = 'Prevencion de Riesgo', _('Prevencion de Riesgo')
        RRHH = 'Recursos Humanos', _('Recursos Humanos')
        RELACIONADAS = 'Relacionadas', _('Relacionadas')
        TESORERIA = 'Tesoreria', _('Tesoreria')
        VENTAS = 'Ventas', _('Ventas')
        
    class Typemarca(models.TextChoices):
        HP = 'HP', _('HP')
        LENOVO = 'Lenovo', _('Lenovo')
        ASUS = 'Asus', _('Asus')
    
    class Typestatus(models.TextChoices):
        ASIGNADO = 'Asignado', _('Asignado')
        DISPONIBLE = 'Dipsonible', _('Disponible')

    status = models.CharField(choices=Typestatus, max_length=20, null=True, blank=False, default='Asignado')
    empresa = models.CharField(choices=Typeempresa, max_length=20, null=True, blank=False, default=0)
    responsable = models.CharField(max_length=20, null=True, blank=False, default=0)
    cargo = models.CharField(max_length=20, null=True, blank=False, default=0)
    area = models.CharField(choices=Typearea, max_length=20, null=True, default=0)
    anydesk = models.IntegerField( null=True, blank=True, default=0)
    rustdesk = models.IntegerField( null=True, blank=True, default=0)
    password = models.CharField(max_length=20, null=True, blank=False, default=0)
    actaentregado = models.IntegerField( null=True, blank=True, default=0)
    fechaentrega = models.DateField(blank=True, null=True)
    actadevolucion = models.IntegerField( null=True, blank=True, default=0)
    fechadevolucion = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=20, null=True, blank=False, default=0)
    marca = models.CharField(choices=Typemarca, max_length=8, null=True, blank=False, default=0)    
    modelo = models.CharField(max_length=20, null=True, blank=False, default=0)
    nserie = models.CharField(max_length=20, null=True, blank=False, default=0)
    nombre_pc = models.CharField(max_length=20, null=True, blank=False, default=0)
    usuario = models.CharField(max_length=20, null=True, blank=False, default=0)
    marcacpu = models.CharField(max_length=20, null=True, blank=False, default=0)
    modelocpu = models.CharField(max_length=20, null=True, blank=False, default=0)
    ghzcpu = models.CharField(max_length=20, null=True, blank=False, default=0)
    gbram = models.IntegerField(null=True, blank=False, default=0)
    ddrx = models.CharField(max_length=6, null=True, blank=False, default=0)
    mhzram = models.IntegerField(null=True, blank=False, default=0)
    macethernet = models.CharField(max_length=18, blank=False, null=True, default=0)
    macwifi = models.CharField(max_length=18, blank=False, null=True, default=0)
    os = models.CharField(max_length=20, blank=False, null=True, default=0)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
    
    def __str__(self):
        return self.empresa

class Planes(models.Model):
    
    class Typemarca(models.TextChoices):
        WOM = 'WOM', _('WOM')
        ENTEL = 'ENTEL', _('ENTEL')
        MOVISTAR = 'MOVISTAR', _('MOVISTAR')
    
    nombre = models.CharField( max_length=50, null=True)
    numero = models.IntegerField( null=True)
    company = models.CharField(choices=Typemarca, max_length=15, null=True)
    
    class Meta:
        verbose_name = 'Planes'
        verbose_name_plural = 'Planes Mobiles'
    
    def __str__(self):
        return self.nombre