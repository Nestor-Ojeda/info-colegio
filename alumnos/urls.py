from django.urls import path
from . import views

urlpatterns = [
    path("", views.alumnos, name="alumnos"),
]
