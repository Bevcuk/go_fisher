# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-18 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20160918_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug_params_json',
            field=models.TextField(blank=True, null=True),
        ),
    ]