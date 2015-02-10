# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cover', models.ImageField(upload_to=b'cover')),
                ('author', models.ManyToManyField(to='author.Author')),
                ('dewey', models.ForeignKey(to='dewey.Dewey')),
                ('publisher', models.ForeignKey(to='publisher.Publisher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
