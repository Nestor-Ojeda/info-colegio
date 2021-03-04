from django.shortcuts import render, HttpResponse, Http404, get_object_or_404,redirect
from .models import Depto
from .forms import DeptoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def deptos(request):
    lista_depto = Depto.objects.all()
    return render(request, "depto/depto.html",{"lista_depto":lista_depto})

def saludo(request):
	template = "depto/saludo.html"
	contexto = {
		"nombre": "Fabian",
		"numero": 1232
	}
	return render(request, template, contexto)

def ver_depto(request, id):
	try:
		dpto = Depto.objects.get(pk=id)
	except Depto.DoesNotExist:
			raise Http404("¡No se ha encontrado!")
	template = "depto/depto.html"
	contexto ={
		"dpto": dpto,
	}
	return render(request, template, contexto)

@login_required
def nue_dpto(request):
	print(request.POST)
	form = DeptoForm()
	if request.method == "POST":
		form = DeptoForm(request.POST)
		if form.is_valid():
			dpto = form.save()
			return redirect("depto:ver_depto", dpto.id)

	contexto = {"form":form}
	template = "depto/nuevo.html"
	return render(request, template, contexto)


def editar_depto(request,id):
    try:
        dpto = Depto.objects.get(pk=id)
    except Depto.DoesNotExist:
        raise Http404("no se encontró")

    if request.method == "GET":
        form = DeptoForm(instance=dpto)

    if request.method == "POST":
        form = DeptoForm(request.POST, instance=dpto)
        if form.is_valid():
            dpto = form.save()
            return redirect("depto:ver_depto", dpto.id)    


    template = "depto/nuevo.html"
    contexto = {"form":form}
    return render(request, template, contexto)


def prueba_base(request):
    return render(request, "base.html", {})