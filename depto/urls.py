from django.urls import path
from . import views

urlpatterns = [
	path("saludo/", views.saludo, name="saludo"),
    path("deptos", views.deptos, name="deptos"),
    path("<int:id>/", views.ver_depto, name="ver_depto"),
    path("nuevo/", views.nue_dpto, name="nue_dpto"),
    path("<int:id>/editar/", views.editar_depto, name="editar_depto"),
    path("prueba_base/", views.prueba_base, name="prueba_base"),
]
