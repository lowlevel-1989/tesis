from django.db import models

class Dewey(models.Model):

	id          = models.IntegerField(primary_key = True)
	description = models.CharField(max_length=45)