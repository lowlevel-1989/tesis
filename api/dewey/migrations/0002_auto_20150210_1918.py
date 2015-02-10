# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dewey', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dewey',
            options={'ordering': ('id',), 'verbose_name': 'Dewey', 'verbose_name_plural': 'Dewey'},
        ),
    ]
