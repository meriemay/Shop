# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 08:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0008_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='product',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]