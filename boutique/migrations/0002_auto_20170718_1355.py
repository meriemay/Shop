# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_favorite',
            new_name='is_activate',
        ),
    ]