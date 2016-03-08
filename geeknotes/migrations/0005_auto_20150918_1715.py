# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Folder = apps.get_model("geeknotes", "Folder")
    db_alias = schema_editor.connection.alias
    Folder.objects.using(db_alias).bulk_create([
        Folder(name="Not Sorted"),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Folder instances,
    # so reverse_func() should delete them.
    Folder = apps.get_model("geeknotes", "Folder")
    db_alias = schema_editor.connection.alias
    Folder.objects.using(db_alias).filter(name="Not Sorted").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('geeknotes', '0004_auto_20150907_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('icon', filer.fields.image.FilerImageField(related_name='foler_image', blank=True, to='filer.Image', null=True)),
            ],
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.AddField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(related_name='notes', default=1, to='geeknotes.Folder'),
        ),
    ]
