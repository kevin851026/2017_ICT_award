# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0025_article_pusher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pusher',
            field=models.TextField(default=''),
        ),
    ]
