# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titre de la note')),
                ('slug', models.SlugField(verbose_name='URL de la note')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de la note')),
                ('auto_create_date', models.DateTimeField(auto_now_add=True)),
                ('auto_update_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='Note')),
            ],
        ),
    ]
