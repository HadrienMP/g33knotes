# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeknotes', '0006_folder_fa'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='slug',
            field=models.SlugField(verbose_name='URL', blank=True),
        ),
    ]
