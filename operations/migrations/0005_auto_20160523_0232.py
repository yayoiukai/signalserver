# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-05-23 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_auto_20160523_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_name',
            field=models.CharField(choices=[('BRO', 'Bronx'), ('BRK', 'Brooklyn'), ('QNS', 'Queens'), ('MAN', 'Manhattan'), ('STN', 'Staten Island')], max_length=20),
        ),
        migrations.AlterField(
            model_name='operation',
            name='variable_name',
            field=models.CharField(choices=[('LAB', 'labor'), ('CAR', 'cars'), ('TRU', 'trucks'), ('WRI', 'writing')], max_length=200),
        ),
    ]