# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Editorial')),
                ('address', models.CharField(max_length=150, verbose_name=b'Direcci\xc3\xb3n')),
                ('city', models.CharField(max_length=60, verbose_name=b'Ciudad')),
                ('state', models.CharField(max_length=30, verbose_name=b'Estado')),
                ('country', models.CharField(max_length=50, verbose_name=b'Pa\xc3\xads')),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
            },
            bases=(models.Model,),
        ),
    ]
