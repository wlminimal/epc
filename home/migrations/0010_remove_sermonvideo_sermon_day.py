# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170609_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sermonvideo',
            name='sermon_day',
        ),
    ]
