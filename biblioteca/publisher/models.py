#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class Publisher(models.Model):
	name    = models.CharField('Editorial', max_length=30  )
	address = models.CharField('Dirección', max_length=150 )
	city    = models.CharField('Ciudad',    max_length=60  )
	state   = models.CharField('Estado',    max_length=30  )
	country = models.CharField('País',      max_length=50  )

	class Meta:
		verbose_name		= 'Editorial'
		verbose_name_plural	= 'Editoriales'

	def __unicode__(self):
		return '%s' % self.name 
