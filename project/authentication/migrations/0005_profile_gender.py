# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
