# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-06-13 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0019_auto_20160613_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='task_id',
            field=models.CharField(max_length=200),
        ),
    ]