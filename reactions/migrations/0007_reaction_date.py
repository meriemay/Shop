# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0006_auto_20170807_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
