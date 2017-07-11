# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2017-07-09 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploads', '0040_auto_20170111_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoMeta',
            fields=[
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fileuploads.Video')),
                ('file_name', models.CharField(max_length=400)),
                ('format_log_name', models.CharField(max_length=400)),
                ('duration', models.CharField(max_length=400, null=True)),
                ('size', models.CharField(max_length=400, null=True)),
                ('bitrate', models.CharField(max_length=400, null=True)),
                ('codec_name', models.CharField(max_length=400)),
                ('codec_type', models.CharField(max_length=400)),
                ('width', models.CharField(max_length=400)),
                ('height', models.CharField(max_length=400)),
                ('sample_aspect_ratio', models.CharField(max_length=400)),
                ('display_aspect_ratio', models.CharField(max_length=400)),
                ('pixel_format', models.CharField(max_length=400)),
                ('field_order', models.CharField(max_length=400)),
                ('average_frame_rate', models.CharField(max_length=400)),
                ('sample_rate', models.CharField(max_length=400, null=True)),
                ('bits_per_raw_sample', models.CharField(max_length=400, null=True)),
                ('channel', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]