from django.db import models

# Create your models here.
class Depto(models.Model):
	nombre = models.CharField(max_length = 50, unique=True)

	def __str__(self):
		text = "{0}"
		return text.format(self.nombre)
