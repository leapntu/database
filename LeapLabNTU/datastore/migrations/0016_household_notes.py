# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0015_householdmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]