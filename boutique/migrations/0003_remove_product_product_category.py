# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_auto_20170718_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
    ]