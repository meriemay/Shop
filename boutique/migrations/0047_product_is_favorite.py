# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0046_auto_20170824_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
