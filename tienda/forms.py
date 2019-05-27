from django import forms
from .models import Clientes

class pedido(forms.ModelForm):
    class Meta :
        model = Clientes
        fields=('Nombre','Telefono','Email','Domicilio',)
       # fields=['Nombre','Telefono','Email','Domicilio',]
       # labels = {'Nombre': 'Nombre','Telefono': 'Telefono','Email': 'Email','Domicilio': 'Domicilio',}
       # widgets = {'Nombre': forms.TextInput(attrs={'class': 'form-control'}),'Telefono': forms.TextInput(attrs={'class': 'form-control'}), 'Email': forms.TextInput(attrs={'class': 'form-control'}),'Domicilio': forms.TextInput(attrs={'class': 'form-control'}), }
