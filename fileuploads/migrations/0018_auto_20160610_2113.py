# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-06-10 21:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0017_delete_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filedata',
            name='filename',
        ),
        migrations.DeleteModel(
            name='Filedata',
        ),
        migrations.DeleteModel(
            name='Filename',
        ),
    ]
