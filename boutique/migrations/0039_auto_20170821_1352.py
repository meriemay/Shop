# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0038_product_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.CharField(blank=True, choices=[('baby', 'BABY [1-3]'), ('child', 'CHILD [4-12]'), ('teenager', 'TEENAGER [13-21]'), ('adult', 'ADULT')], default=None, max_length=10),
        ),
    ]
