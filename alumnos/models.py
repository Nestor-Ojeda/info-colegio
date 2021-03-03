from django.db import models
from domicilio.models import Direccion
from contactos.models import Contacto
from personas.models import Persona
# Create your models here.
class TutorA(models.Model):
	parentesco = models.CharField(max_length = 100)
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL,
        null=True, related_name="pers1")
	telefono = models.ForeignKey(Contacto, on_delete=models.SET_NULL,
        null=True, related_name="telefono1")
	email = models.EmailField()
	domicilio = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		tex = "{0}-{1}-{2}-{3}-{4}"
		return tex.format(self.parentesco, self.persona, self.telefono, self.email, self.domicilio)
	
class TutorB(models.Model):
	parentesco = models.CharField(max_length = 100)
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL,
        null=True, related_name="pers2")
	telefono = models.ForeignKey(Contacto, on_delete=models.SET_NULL,
        null=True, related_name="telefono2")
	email = models.EmailField()
	domicilio = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		tex = "{0}-{1}-{2}-{3}-{4}"
		return tex.format(self.parentesco, self.persona, self.telefono,self.email, self.domicilio)

class Alumno(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL,
        null=True, related_name="pers3")
	nacimiento = models.DateField()
	telefono = models.ForeignKey(Contacto, on_delete=models.SET_NULL,
        null=True, related_name="telefono3")
	email = models.EmailField()
	domicilio = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
	tutor_a = models.ForeignKey(TutorA, on_delete=models.SET_NULL, null=True, related_name="a")
	tutor_b = models.ForeignKey(TutorB, on_delete=models.SET_NULL, null=True, related_name="b")

	def __str__(self):
		tex = "{0}-{1}-{2}-{3}-{4}-{5}-{6}"
		return tex.format(self.persona, self.nacimiento, self.telefono, self.email, self.domicilio, self.tutor_a, self.tutor_b)
