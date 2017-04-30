# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-30 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0008_auto_20170429_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrecord',
            name='count',
            field=models.IntegerField(default=1, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.CharField(choices=[('pass', '\u901a\u8fc7'), ('reject', '\u672a\u901a\u8fc7'), ('waiting', '\u7b49\u5f85\u5ba1\u6838')], default='waiting', max_length=20, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='status',
            field=models.CharField(choices=[('pass', '\u901a\u8fc7'), ('reject', '\u672a\u901a\u8fc7'), ('waiting', '\u7b49\u5f85\u5ba1\u6838')], default='waiting', max_length=20, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workload.Work', verbose_name='\u5de5\u65f6\u7c7b\u578b'),
        ),
    ]
