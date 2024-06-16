from django.shortcuts import render, get_object_or_404
from .models import Producto

def principal(request):
    return render(request, 'principal.html')

def producto(request, categoria):
    productos = Producto.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'productos': productos,
    }
    return render(request, 'producto.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def simulador(request):
    return render(request, 'simulador.html')
from page.models import Producto

