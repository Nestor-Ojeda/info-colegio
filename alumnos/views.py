from django.shortcuts import render
from .models import Alumno
# Create your views here.
def alumnos(request):
    lista_alumnos = Alumno.objects.all()
    return render(request, "alumnos/alumnos.html",{"lista_alumnos":lista_alumnos})
