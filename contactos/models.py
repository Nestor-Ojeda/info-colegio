from django.db import models
from personas.models import Persona
# Create your models here.

class Contacto(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL,
        null=True, related_name="perss")
	numero = models.IntegerField(max_length = 16)

	def __str__(self):
		tex = "{0}-{1}"
		return tex.format(self.persona, self.numero)

	