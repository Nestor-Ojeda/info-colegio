from django.shortcuts import render
from .models import Contacto
# Create your views here.
def contactos(request):
    lista_contactos = Contacto.objects.all()
    return render(request, "contactos/contactos.html",{"lista_contactos":lista_contactos})
