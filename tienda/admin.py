from django.contrib import admin
from .models import Productos
from .models import Clientes


admin.site.register(Productos)
admin.site.register(Clientes)
