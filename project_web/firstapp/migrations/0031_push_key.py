# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0030_auto_20171018_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='push',
            name='key',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='firstapp.article'),
            preserve_default=False,
        ),
    ]
