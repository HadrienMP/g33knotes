# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('geeknotes', '0003_auto_20150618_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', filer.fields.file.FilerFileField(related_name='attachment_file', to='filer.File')),
            ],
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-create_date']},
        ),
        migrations.AlterField(
            model_name='note',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(verbose_name='URL', blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titre'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='note',
            field=models.ForeignKey(related_name='attachments', to='geeknotes.Note'),
        ),
    ]
