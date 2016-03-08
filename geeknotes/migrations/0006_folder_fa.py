# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeknotes', '0005_auto_20150918_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='fa',
            field=models.CharField(max_length=100, verbose_name='Ic\xf4ne font awesome', blank=True),
        ),
    ]
