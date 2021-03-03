from django.shortcuts import render
from .models import Personal

# Create your views here.
def personal(request):
    lista_personal = Personal.objects.all()
    return render(request, "personal/personal.html",{"lista_personal":lista_personal})
