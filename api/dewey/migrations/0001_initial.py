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
                ('description', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
