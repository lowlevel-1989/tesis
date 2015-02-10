from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name  = models.CharField(max_length=30)

	def __unicode__(self):
		return '%s %s' % (self.last_name, self.first_name)