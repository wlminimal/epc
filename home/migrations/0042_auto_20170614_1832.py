# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-14 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20170614_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_hero_description',
            field=wagtail.core.fields.RichTextField(default='Description'),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_hero_subtitle',
            field=models.TextField(default='요한 계시록 강해 / 특별 강사 설교'),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_hero_title',
            field=models.CharField(default='금요 예배 설교 영상', max_length=80),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_main_title_1',
            field=models.CharField(default='최신 주일 예배 설교 영상', max_length=100),
        ),
        migrations.AddField(
            model_name='fridaysermonpage',
            name='f_sermon_main_title_2',
            field=models.CharField(default='지난 주일 예배 설교 영상들', max_length=100),
        ),
        migrations.AddField(
            model_name='lorddaysermonpage',
            name='sermon_hero_description',
            field=wagtail.core.fields.RichTextField(default='Description'),
        ),
        migrations.AddField(
            model_name='lorddaysermonpage',
            name='sermon_hero_subtitle',
            field=models.TextField(default='성경을 성경으로 해석한다'),
        ),
        migrations.AddField(
            model_name='lorddaysermonpage',
            name='sermon_hero_title',
            field=models.CharField(default='주일 설교 영상', max_length=80),
        ),
        migrations.AddField(
            model_name='lorddaysermonpage',
            name='sermon_main_title_1',
            field=models.CharField(default='최신 주일 예배 설교 영상', max_length=100),
        ),
        migrations.AddField(
            model_name='lorddaysermonpage',
            name='sermon_main_title_2',
            field=models.CharField(default='지난 주일 예배 설교 영상들', max_length=100),
        ),
    ]
