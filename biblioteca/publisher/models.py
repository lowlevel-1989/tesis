#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class Publisher(models.Model):
	name    = models.CharField('Editorial', max_length=30  )

	class Meta:
		verbose_name		= 'Editorial'
		verbose_name_plural	= 'Editoriales'

	def __unicode__(self):
		return '%s' % self.name 
