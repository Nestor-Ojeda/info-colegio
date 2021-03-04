from django.urls import path
from . import views

app_name = "perfil"
urlpatterns = [
    path("login/", views.iniciar_sesion, name="login"),
    path("logout/", views.cerrar_sesion, name="logout"),
]
