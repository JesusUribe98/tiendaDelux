from django.shortcuts import render
from .models import Productos
from .models import Clientes
from django.views.generic import CreateView
from .forms import pedido
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request,"tienda/index.html")

def info(request):
    return render(request,"tienda/info.html")

#def compra(request):
 #   return render(request,"tienda/Compra.html")

#crud productos

def productos_list(request):

    productos=Productos.objects.all()

    return render(request,"tienda/productos_list.html", {'productos':productos})

#class compra2(CreateView):
def compra2(request):
    #model = Clientes
    #form_class = pedido
    if request.method == "POST":
   	 #form = pedido()
   	 form = pedido(request.POST)
   	 if form.is_valid():
            post = form.save(commit=False)
            post.save()
            success_url = reverse_lazy("/")
    else:
        form = pedido()
    return render(request,'tienda/Compra.html',{'form': form})
    success_url = reverse_lazy("/")
    #template_name = 'tienda/Compra.html'

