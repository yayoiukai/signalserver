# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-10-03 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20161003_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user_name',
            field=models.CharField(default=123, max_length=400),
            preserve_default=False,
        ),
    ]