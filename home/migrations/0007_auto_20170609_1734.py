# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_sermonvideos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SermonVideos',
            new_name='SermonVideo',
        ),
    ]
