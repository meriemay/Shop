# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
    ]