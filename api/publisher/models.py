from django.db import models

class Publisher(models.Model):
	name    = models.CharField('Nombre',    max_length=30)
	address = models.CharField('Direccion', max_length=150)
	city    = models.CharField('Ciudad',    max_length=60)
	state   = models.CharField('Estado',    max_length=30)
	country = models.CharField('Pais',      max_length=50)

	def __unicode__(self):
		return '%s' % self.name 
