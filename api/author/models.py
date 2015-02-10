from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=60)

	def __unicode__(self):
		return '%s' % self.name