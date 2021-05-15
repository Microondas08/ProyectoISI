from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Servicio


# Register your models here.

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, servicioAdmin)