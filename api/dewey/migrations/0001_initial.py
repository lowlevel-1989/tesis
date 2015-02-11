# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dewey',
            fields=[
                ('id', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=45, verbose_name=b'Descripcion')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Dewey',
                'verbose_name_plural': 'Dewey',
            },
            bases=(models.Model,),
        ),
    ]
