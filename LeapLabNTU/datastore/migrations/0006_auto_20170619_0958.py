# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0005_parent_occupation_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='occupation',
        ),
        migrations.AlterField(
            model_name='parent',
            name='occupation_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datastore.Occupation'),
        ),
    ]
