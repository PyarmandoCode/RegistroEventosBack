from django.contrib import admin
from .models import Empleados, Eventos, Areas, Cia,Estacionamiento,Departamentos

admin.site.register([Empleados, Eventos, Areas, Cia])

admin.site.site_header = "Empresa XYZ"
admin.site.site_title = "Empresa XYZ"
admin.site.index_title = "Bienvenido a la Zona de Administrador"

