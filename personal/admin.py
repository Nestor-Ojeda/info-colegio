from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Personal)
class EmpleadoAdmin(admin.ModelAdmin):
	pass
