from django.db import models

class Dewey(models.Model):
	id          = models.CharField(max_length=3, primary_key = True)
	description = models.CharField(max_length=45)

	def __unicode__(self):
		return '%s - %s' % ( self.id, self.description) 