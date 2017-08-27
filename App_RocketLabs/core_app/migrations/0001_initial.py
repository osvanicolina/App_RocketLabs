# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='knows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_level', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=70)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('linkedln_link', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True, max_length=255)),
                ('secret_link', models.CharField(max_length=50, unique=True)),
                ('photo', models.ImageField(upload_to=b'')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_team_member', models.BooleanField(default=False)),
                ('failed_logins', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('is_blocked', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=30)),
                ('telephone_number', models.DecimalField(blank=True, decimal_places=0, max_digits=13)),
                ('requester_mail', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('client_user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('skill_logo', models.ImageField(upload_to=b'')),
                ('about', models.TextField(max_length=255)),
                ('users', models.ManyToManyField(through='core_app.knows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='knows',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.Skill'),
        ),
        migrations.AddField(
            model_name='knows',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
