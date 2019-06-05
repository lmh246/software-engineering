# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-05-02 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdverTise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('capital', models.IntegerField(max_length=100)),
                ('duration', models.IntegerField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
    ]
