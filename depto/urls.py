from django.urls import path
from . import views

urlpatterns = [
    path("", views.deptos, name="deptos"),
]
