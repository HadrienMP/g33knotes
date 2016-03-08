# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeknotes', '0002_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='html',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(verbose_name='URL de la note', blank=True),
        ),
    ]
