# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-09-14 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0030_auto_20160814_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='shared',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='result',
            name='user_name',
            field=models.CharField(default=None, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='shared',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='user_name',
            field=models.CharField(default=None, max_length=400, null=True),
        ),
    ]