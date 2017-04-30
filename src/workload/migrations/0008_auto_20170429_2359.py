# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0007_workrecord_tmp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workrecord',
            name='tmp',
        ),
        migrations.AddField(
            model_name='workrecord',
            name='short',
            field=models.CharField(blank=True, max_length=300, verbose_name='\u7b80\u77ed\u63cf\u8ff0'),
        ),
    ]