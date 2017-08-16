# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0008_auto_20170719_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='label',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, choices=[('Clothing_and_accessories', 'Clothing_and_accessories'), ('Jewelry', 'Jewelry'), ('Creative_Supply', 'Creative_Supply'), ('weddings', 'weddings'), ('House', 'House'), ('Child_and_Baby', 'Child_and_Baby')], default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='boutique.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('Hand Made', 'Hand Made'), ('Vintage', 'Vintage')], default=None, max_length=20),
        ),
    ]