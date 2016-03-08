# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeknotes', '0007_folder_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='fa',
            field=models.CharField(max_length=100, verbose_name='FA Icon', blank=True),
        ),
    ]
