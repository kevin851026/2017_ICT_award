# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0031_push_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='push',
            name='key',
        ),
    ]