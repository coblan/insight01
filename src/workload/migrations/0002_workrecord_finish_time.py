# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-13 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrecord',
            name='finish_time',
            field=models.CharField(blank=True, max_length=20, verbose_name='\u5b8c\u6210\u65f6\u95f4'),
        ),
    ]
