from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=30)
	country = models.CharField(max_length=50)

	def __unicode__(self):
		return '%s' % self.name 
