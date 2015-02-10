from django.db import models
from author.models import Author
from dewey.models import Dewey
from publisher.models import Publisher 

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	isbn = models.CharField(max_length=13)
	dewey = models.ForeignKey(Dewey)
	pages = models.IntegerField()
	year = models.IntegerField()
	cover = models.ImageField(upload_to = 'cover')

	def __unicode__(self):
		return '%s' % self.title