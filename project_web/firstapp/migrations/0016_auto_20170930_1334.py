# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-30 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_auto_20170930_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blue_n',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='article',
            name='blue_p',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]
