# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0033_auto_20170818_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.TextField(blank=True, default=None, max_length=250),
        ),
    ]