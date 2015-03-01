#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError

def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1] # [0] returns path+filename
	valid_extensions = ('.pdf', )
	if not ext in valid_extensions:
		raise ValidationError('Extensión no pertida.')

def validate_file_image(value):
	import os
	ext = os.path.splitext(value.name)[1] # [0] returns path+filename
	valid_extensions = ('.jpg', 'png', )
	if not ext in valid_extensions:
		raise ValidationError('Extensión no pertida.')