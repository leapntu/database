# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0004_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='occupation_link',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='datastore.Occupation'),
            preserve_default=False,
        ),
    ]
