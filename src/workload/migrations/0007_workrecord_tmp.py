# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0006_auto_20170429_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrecord',
            name='tmp',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u4e34\u65f6\u6027\u5de5\u4f5c'),
        ),
    ]