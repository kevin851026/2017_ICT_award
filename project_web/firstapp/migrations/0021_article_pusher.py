# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0020_auto_20171016_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pusher',
            field=models.TextField(default=None),
        ),
    ]