from django.shortcuts import render
from .models import Persona

# Create your views here.
def persona(request):
    lista_persona = Persona.objects.all()
    return render(request, "personas/persona.html",{"lista_persona":lista_persona})
