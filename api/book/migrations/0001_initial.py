# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import book.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dewey', '0001_initial'),
        ('author', '0001_initial'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titulo')),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField(verbose_name=b'P\xc3\xa1ginas')),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o')),
                ('public', models.BooleanField(default=False, verbose_name=b'P\xc3\xbablico')),
                ('cover', models.ImageField(upload_to=b'cover/%Y/%m/%d', verbose_name=b'Portada')),
                ('book_pdf', models.FileField(upload_to=b'documents/%Y/%m/%d', verbose_name=b'Libro_pdf', validators=[book.validators.validate_file_extension])),
                ('author', models.ManyToManyField(to='author.Author', verbose_name=b'Autores')),
                ('dewey', models.ForeignKey(to='dewey.Dewey')),
                ('publisher', models.ForeignKey(verbose_name=b'Editorial', to='publisher.Publisher')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
            bases=(models.Model,),
        ),
    ]
