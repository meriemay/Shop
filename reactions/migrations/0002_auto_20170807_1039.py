# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boutique.Product'),
        ),
    ]
