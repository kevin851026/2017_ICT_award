# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_auto_20170928_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='board',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
    ]
