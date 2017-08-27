# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bundles_app', '0001_initial'),
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
                ('str_duration', models.CharField(blank=True, max_length=50)),
                ('estimated_duration', models.CharField(blank=True, max_length=50)),
                ('done_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('current_stage', models.CharField(blank=True, max_length=50)),
                ('is_complete', models.BooleanField(default=False)),
                ('owner_comment', models.TextField(blank=True, max_length=500)),
                ('demo_link', models.CharField(blank=True, max_length=100)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(blank=True)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bundles_app.Bundle')),
                ('owner_profiles', models.ManyToManyField(db_table='projects_app_owner_profiles', to='core_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('screenshot', models.ImageField(upload_to=b'')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_app.Project')),
            ],
        ),
    ]
