# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-05-09 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_articletable_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentstable',
            name='article_id',
        ),
        migrations.RemoveField(
            model_name='commentstable',
            name='user_id',
        ),
        migrations.AddField(
            model_name='articletable',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articletable',
            name='avg_grade',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='CommentsTable',
        ),
    ]
