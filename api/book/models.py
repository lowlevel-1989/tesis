#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from author.models import Author
from dewey.models import Dewey
from publisher.models import Publisher 

class Book(models.Model):
	title     = models.CharField('Titulo', max_length=100)
	author    = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	isbn      = models.CharField(max_length=13)
	dewey     = models.ForeignKey(Dewey)
	pages     = models.IntegerField('Páginas')
	year      = models.IntegerField('Año')
	cover     = models.ImageField('Portada', upload_to = 'cover')

	class Meta:
		verbose_name		= 'Libro'
		verbose_name_plural	= 'Libros'

	def __unicode__(self):
		return '%s' % self.title