from django.contrib import admin
from .models import Casa, Photos
# Register your models here.
class CasasImageAdmin(admin.StackedInline):
    model = Photos
    
@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    inlines = [CasasImageAdmin]
    
    class meta:
        model = Casa
        
@admin.register(Photos)
class CasasImageAdmin(admin.ModelAdmin):
    pass
