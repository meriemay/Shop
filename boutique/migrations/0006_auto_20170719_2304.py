# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0005_auto_20170719_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(choices=[('CA', 'Clothing_and_accessories'), ('J', 'Jewelry'), ('CS', 'Creative_Supply'), ('W', 'weddings'), ('H', 'House'), ('CB', 'Child_and_Baby')], default=None, on_delete=django.db.models.deletion.CASCADE, to='boutique.Category'),
        ),
    ]
