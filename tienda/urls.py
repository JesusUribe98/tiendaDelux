from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("info/",views.info, name="informacion"),
    path("productos/",views.productos_list, name="productos"),
    path("comprar/",views.compra2, name="comprar"),
]