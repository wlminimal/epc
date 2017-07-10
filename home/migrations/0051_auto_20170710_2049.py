# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20170710_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fridaysermonpage',
            name='f_sermon_main_title_1',
        ),
        migrations.RemoveField(
            model_name='fridaysermonpage',
            name='f_sermon_main_title_2',
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_1',
            field=models.CharField(default='요한 계시록', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_1_main_title_1',
            field=models.CharField(default='최신 요한계시록 강해 영상', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_1_main_title_2',
            field=models.CharField(default='지난 요한계시록 강해 영상들', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_2',
            field=models.CharField(default='로마서', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_2_main_title_1',
            field=models.CharField(default='최신 로마서 강해 영상', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_2_main_title_2',
            field=models.CharField(default='지난 로마서 강해 영상들', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_3',
            field=models.CharField(default='빌립보서', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_3_main_title_1',
            field=models.CharField(default='최신 빌립보서 강해 영상', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_3_main_title_2',
            field=models.CharField(default='지난 빌립보서 강해 영상들', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_4',
            field=models.CharField(default='시편', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_4_main_title_1',
            field=models.CharField(default='최신 시편 강해 영상', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_bible_4_main_title_2',
            field=models.CharField(default='지난 시편 강해 영상들', max_length=100),
        ),
    ]