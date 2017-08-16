# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_auto_20170719_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.CharField(choices=[('CA', 'Clothing_and_accessories'), ('J', 'Jewelry'), ('CS', 'Creative_Supply'), ('W', 'weddings'), ('H', 'House'), ('CB', 'Child_and_Baby')], max_length=250, unique=True),
        ),
    ]