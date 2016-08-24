# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-14 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_subcategory_extra_parameters'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]