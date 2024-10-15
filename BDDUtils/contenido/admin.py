from django.contrib import admin
from .models import sesionremota, nubecorporativa, cuentas, dominios, cuentas_admin, cuentas_ope, direccionamiento

# Register your models here.
class dominiosAdm(admin.ModelAdmin):
    list_display = ("dominio", "enlace", "usuario", "password")
    search_fields = ["dominio", "enlace"]
    sortable_by = ("dominio")
    
admin.site.register(dominios, dominiosAdm)

class sesionremotaAdm(admin.ModelAdmin):
    list_display = ("nombre", "usuario", "password", "colaborador", "sistema", "certificados")
    list_filter = ("nombre","usuario")
    search_fields = ["nombre", "usuario"]
    sortable_by = ("nombre")

admin.site.register(sesionremota, sesionremotaAdm)

class nubecoperacionAdm(admin.ModelAdmin):
    list_display = ("cuenta", "password", "departamentos")
    search_fields = ["cuenta"]
    sortable_by = ("cuenta")

admin.site.register(nubecorporativa, nubecoperacionAdm)

class cuentasAdm(admin.ModelAdmin):
    list_display = ("plataforma", "cuenta", "password")
    search_fields = ["cuenta"]
    sortable_by = ("plataforma")

admin.site.register(cuentas, cuentasAdm)

class cuentas_adminAdm(admin.ModelAdmin):
    list_display = ("nombre", "correo", "password", "tipo_cargo", "cargo", "passzoho")
    search_fields = ["nombre", "correo"]
    list_filter = ("nombre", "correo")
    sortable_by = ("nombre")

admin.site.register(cuentas_admin, cuentas_adminAdm)

class cuentas_opeAdm(admin.ModelAdmin):
    list_display = ("nombre", "correo", "password", "tipo_cargo", "cargo", "passzoho")
    list_filter = ("nombre", "correo")
    search_fields = ["nombre", "correo"]
    sortable_by = ("nombre")

admin.site.register(cuentas_ope, cuentas_opeAdm)

class direccionamientoAdm(admin.ModelAdmin):
    list_display = ("ip", "nombre_dispositivo", "descripcion", "mac")
    search_fields = ["ip"]
    sortable_by = ("ip")

admin.site.register(direccionamiento, direccionamientoAdm)