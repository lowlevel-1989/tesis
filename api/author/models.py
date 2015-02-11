#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class Author(models.Model):
	name = models.CharField('Nombre Completo', max_length=60)

	class Meta:
		verbose_name		= 'Autor'
		verbose_name_plural	= 'Autores'

	def __unicode__(self):
		return '%s' % self.name