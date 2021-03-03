from django.shortcuts import render
from .models import Depto

# Create your views here.
def deptos(request):
    lista_depto = Depto.objects.all()
    return render(request, "depto/depto.html",{"lista_depto":lista_depto})
