#!/usr/bin/python
# -*- coding: utf-8 -*-

from .validators import validate_file_extension

from django.db        import models
from author.models    import Author
from dewey.models     import Dewey
from publisher.models import Publisher 


class Book(models.Model):
	title     = models.CharField       ( 'Titulo',               max_length=100                                            )
	isbn      = models.CharField       (                         max_length=13                                             )
	dewey     = models.ForeignKey      (              Dewey                                                                )
	author    = models.ManyToManyField (              Author,                   verbose_name='Autores'                     )
	publisher = models.ForeignKey      (              Publisher,                verbose_name='Editorial'                   )
	pages     = models.IntegerField    ( 'Páginas'                                                                         )
	year      = models.IntegerField    ( 'Año'                                                                             )
	public    = models.BooleanField    ( 'Público',   default=False                                                        )
	cover     = models.ImageField      ( 'Portada',   upload_to='cover/%Y/%m/%d'                                           )
	book_pdf  = models.FileField       ( 'Libro_pdf', upload_to='documents/%Y/%m/%d', validators=[validate_file_extension] )

	class Meta:
		verbose_name		= 'Libro'
		verbose_name_plural	= 'Libros'

	def pais(self):
		return '%s' % self.publisher.country

	def portada(self):
		return """
			<a href="%s" target="_blank"><img src="%s" width="90" height="120" /></a>
		""" % (self.cover.url, self.cover.url)

	portada.allow_tags = True

	def __unicode__(self):
		return '%s' % self.title