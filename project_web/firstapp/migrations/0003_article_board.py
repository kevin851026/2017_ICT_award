# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20170704_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='board',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]