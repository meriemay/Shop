# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 12:13
from __future__ import unicode_literals

import boutique.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0018_auto_20170720_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_logo',
            field=models.ImageField(null=True, upload_to=boutique.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_logo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
