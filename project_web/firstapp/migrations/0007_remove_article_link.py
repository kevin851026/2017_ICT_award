# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='link',
        ),
    ]