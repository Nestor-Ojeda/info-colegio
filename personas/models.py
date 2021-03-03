from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	edad = models.IntegerField()
	dni = models.CharField(max_length = 9)

	def __str__(self):
		tex = "{0}-{1}-{2}-{3}"
		return tex.format(self.nombre, self.apellido, self.edad, self.dni)


