# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0012_auto_20170619_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='baby',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baby',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
