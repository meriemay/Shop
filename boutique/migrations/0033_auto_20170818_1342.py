# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0032_auto_20170818_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
