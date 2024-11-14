from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
from .models import *
import xlsxwriter

def download_excel(modeladmin, request, queryset):
    model_name = modeladmin.model.__name__
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={model_name}.xlsx'
    
    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()
    
    headers = [field.verbose_name for field in modeladmin.model._meta.fields]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)
        
    for row_num, obj in enumerate(queryset, 1):
        for col_num, field in enumerate(modeladmin.model._meta.fields):
            value = str(getattr(obj, field.name))
            worksheet.write(row_num, col_num, value)
            
    workbook.close()
    return response

download_excel.short_description = "Download selected items as Excel"

# Register your models here.
class dominiosAdm(admin.ModelAdmin):
    list_display = ["dominio", "enlace", "usuario", "password"]
    search_fields = ["dominio", "enlace"]
    sortable_by = ("dominio")
    
    actions = [download_excel]

admin.site.register(dominios, dominiosAdm)

class sesionremotaAdm(admin.ModelAdmin):
    list_display = ("nombre", "usuario", "password", "colaborador", "sistema", "certificados")
    list_filter = ("nombre","usuario")
    search_fields = ["nombre", "usuario"]
    sortable_by = ("nombre")
    
    actions = [download_excel]

admin.site.register(sesionremota, sesionremotaAdm)

class nubecoperacionAdm(admin.ModelAdmin):
    list_display = ("cuenta", "password", "departamentos")
    search_fields = ["cuenta"]
    sortable_by = ("cuenta")
    
    actions = [download_excel]

admin.site.register(nubecorporativa, nubecoperacionAdm)

class cuentasAdm(admin.ModelAdmin):
    list_display = ("plataforma", "cuenta", "password")
    search_fields = ["cuenta"]
    sortable_by = ("plataforma")
    
    actions = [download_excel]

admin.site.register(cuentas, cuentasAdm)

class cuentas_adminAdm(admin.ModelAdmin):
    list_display = ("nombre", "correo", "password", "tipo_cargo", "cargo", "passzoho")
    search_fields = ["nombre", "correo"]
    list_filter = ("nombre", "correo")
    sortable_by = ("nombre")
    
    actions = [download_excel]

admin.site.register(cuentas_admin, cuentas_adminAdm)

class cuentas_opeAdm(admin.ModelAdmin):
    list_display = ("nombre", "correo", "password", "tipo_cargo", "cargo", "passzoho")
    list_filter = ("nombre", "correo")
    search_fields = ["nombre", "correo"]
    sortable_by = ("nombre")
    
    actions = [download_excel]

admin.site.register(cuentas_ope, cuentas_opeAdm)

class direccionamientoAdm(admin.ModelAdmin):
    list_display = ("ip", "nombre_dispositivo", "descripcion", "mac")
    search_fields = ["ip"]
    sortable_by = ("ip")
    
    actions = [download_excel]

admin.site.register(direccionamiento, direccionamientoAdm)

class inventarioAdm(admin.ModelAdmin):
    list_display = ("empresa","responsable","cargo","area","anydesk","rustdesk","password","actaentregado","fechaentrega","actadevolucion","fechadevolucion","tipo","marca","modelo","nserie","nombre_pc","usuario","marcacpu","modelocpu","ghzcpu","gbram","ddrx","mhzram","macethernet","macwifi","os")
    sortable_by = ("responsable")
    
    actions = [download_excel]
    
admin.site.register(inventario, inventarioAdm)
