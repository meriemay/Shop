# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0019_auto_20170721_1313'),
        ('messenger', '0005_auto_20170727_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boutique.Product'),
        ),
    ]
