from django.db import models
from depto.models import Depto
from domicilio.models import Direccion
from contactos.models import Contacto
from personas.models import Persona
# Create your models here.

class Personal(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL,
        null=True, related_name="pers")
	nacimiento = models.DateField()
	telefono = models.ForeignKey(Contacto, on_delete=models.SET_NULL,
        null=True, related_name="telefono")
	email = models.EmailField()
	sueldo = models.DecimalField(max_digits=10, decimal_places=2)
	depto = models.ForeignKey(Depto, on_delete=models.SET_NULL,
        null=True)
	direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL,
        null=True, related_name="direccion")

	def __str__(self):
		text = "{0}-{1}-{2}-{3}-{4}-{5}-{6}-"
		return text.format(self.persona,
			self.nacimiento, self.telefono, self.email,
			 self.sueldo, self.depto, self.direccion)

