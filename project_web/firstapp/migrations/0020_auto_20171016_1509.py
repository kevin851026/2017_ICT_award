# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_auto_20171016_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='push',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
