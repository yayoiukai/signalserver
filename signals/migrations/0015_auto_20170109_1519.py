# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2017-01-09 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0014_output_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Process',
        ),
        migrations.RenameField(
            model_name='output',
            old_name='request',
            new_name='process',
        ),
    ]
