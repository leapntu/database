# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0014_baby_medical_history_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseholdMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_with_baby', models.TextField()),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('household', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='datastore.Household')),
            ],
        ),
    ]
