# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0024_product_reaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reaction',
        ),
        migrations.DeleteModel(
            name='Reaction',
        ),
    ]
