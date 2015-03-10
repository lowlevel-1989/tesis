#!/usr/bin/python
# -*- coding: utf-8 -*-
from .validators import validate_file_image

from django.db        import models
from author.models    import Author

class Magazine(models.Model):
    id        = models.AutoField       ( 'Registro',                            primary_key = True                                     )
    title     = models.CharField       ( 'Titulo',               max_length=100                                                        )
    isbn      = models.CharField       (                         max_length=13                                                         )
    author    = models.ManyToManyField (              Author,                   verbose_name='Autores'                                 )
    ubication = models.CharField       ( 'Ubicación',            max_length=150                                                        )
    vol       = models.IntegerField    ( 'Volumen'                                                                                     )
    year      = models.IntegerField    ( 'Año'                                                                                         )
    cover     = models.FileField       ( 'Portada',   upload_to='cover/%Y/%m/%d',     validators=[validate_file_image]                 )
    note      = models.TextField       ( 'Nota',                                                                            blank=True )


    class Meta:
        verbose_name        = 'Revista'
        verbose_name_plural = 'Revistas'

    def portada(self):
        return """
            <a href="%s" target="_blank"><img src="%s" width="90" height="120" /></a>
        """ % (self.cover.url, self.cover.url)

    portada.allow_tags = True

    def __unicode__(self):
        return '%s' % self.title