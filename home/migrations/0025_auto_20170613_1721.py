# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20170613_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='service_button_text',
            field=models.CharField(default='See more Service info', max_length=30),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service_lord_day',
            field=models.CharField(default="Lord's Day", max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service_subtitle',
            field=models.CharField(default='Service Schedule', max_length=50),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service_title',
            field=models.CharField(default='EPC Worship Service', max_length=50),
        ),
    ]
