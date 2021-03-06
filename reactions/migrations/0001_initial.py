# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boutique', '0025_auto_20170803_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(blank=True, choices=[('like', 'like'), ('wish', 'wish'), ('share', 'share')], default=None, max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.Product')),
            ],
        ),
    ]
