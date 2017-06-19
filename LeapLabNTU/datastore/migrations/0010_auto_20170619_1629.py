# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0009_auto_20170619_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='baby',
            name='slug',
            field=models.SlugField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='babylanguageprofile',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]