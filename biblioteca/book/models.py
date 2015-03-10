#!/usr/bin/python
# -*- coding: utf-8 -*-
from .validators import validate_file_extension, validate_file_image
from .files      import FileField


from django.db        import models
from django.conf      import settings
from author.models    import Author
from dewey.models     import Dewey
from publisher.models import Publisher 

class Book(models.Model):
    id        = models.AutoField       ( 'Registro',                            primary_key = True                                     )
    title     = models.CharField       ( 'Titulo',               max_length=100                                                        )
    isbn      = models.CharField       (                         max_length=13                                                         )
    dewey     = models.ForeignKey      (              Dewey,                    verbose_name='Cota'                                    )
    author    = models.ManyToManyField (              Author,                   verbose_name='Autores'                                 )
    publisher = models.ForeignKey      (              Publisher,                verbose_name='Editorial'                               )
    ubication = models.CharField       ( 'Ubicación',            max_length=150                                                        )
    year      = models.IntegerField    ( 'Año'                                                                                         )
    pages     = models.IntegerField    ( 'Páginas'                                                                                     )
    cover     = models.FileField       ( 'Portada',   upload_to='cover/%Y/%m/%d',     validators=[validate_file_image]                 )
    book_pdf  =        FileField       ( 'Libro pdf', upload_to='documents/%Y/%m/%d', validators=[validate_file_extension], blank=True )
    note      = models.TextField       ( 'Nota',                                                                            blank=True )
    public    = models.BooleanField    ( 'Público',   default=False                                                                    )


    class Meta:
        verbose_name        = 'Libro'
        verbose_name_plural = 'Libros'

    def portada(self):
        if self.public and self.book_pdf.url != settings.MEDIA_URL:
            link = self.book_pdf.url
        else:
            link = self.cover.url

        return """
            <a href="%s" target="_blank"><img src="%s" width="90" height="120" /></a>
        """ % (link, self.cover.url)

    portada.allow_tags = True

    def __unicode__(self):
        return '%s' % self.title