# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0009_auto_20170908_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]
