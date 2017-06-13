# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0029_koreanschoolpage_nicaraguapage_tiupage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='about_hero_title_1',
            field=models.CharField(default='경건한 예배', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_hero_title_2',
            field=models.CharField(default='성경 중심적 설교', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_hero_title_3',
            field=models.CharField(default='이웃을 섬기는 교회', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_main_title',
            field=models.CharField(default='섬기는 목사님들', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='history_card_title',
            field=models.TextField(default='history of our church'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='history_content',
            field=wagtail.wagtailcore.fields.RichTextField(default='History of our church'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='history_scripture',
            field=models.TextField(default='Scripture for History section'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='history_title',
            field=models.CharField(default='교회 연혁', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='history_verse',
            field=models.CharField(default='Act 20:28', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_message_1',
            field=wagtail.wagtailcore.fields.RichTextField(default='목사님들 인사말씀'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_message_2',
            field=wagtail.wagtailcore.fields.RichTextField(default='목사님들 인사말씀'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_name_1',
            field=models.CharField(default='김정오 목사', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_name_2',
            field=models.CharField(default='나은수 목사', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_picture_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_picture_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_title_1',
            field=models.CharField(default='동부교회 담임목사', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='pastor_title_2',
            field=models.CharField(default='동부교회 목사', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_day_1',
            field=models.CharField(default="Lord's Day", max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_day_2',
            field=models.CharField(default='Friday Day', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_day_3',
            field=models.CharField(default='Saturday Day', max_length=50),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_gen_1',
            field=models.CharField(default='Adult', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_gen_2',
            field=models.CharField(default='Youth Group', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_gen_3',
            field=models.CharField(default='Elementary', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_gen_4',
            field=models.CharField(default='Kinder', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_gen_5',
            field=models.CharField(default='Kinder', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_main_title',
            field=models.CharField(default='Information about Service', max_length=80),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_1',
            field=models.CharField(default='5:30 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_10',
            field=models.CharField(default='2:00 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_11',
            field=models.CharField(default='11:00 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_12',
            field=models.CharField(default='7:30 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_13',
            field=models.CharField(default='5:30 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_2',
            field=models.CharField(default='9:30 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_3',
            field=models.CharField(default='11:00 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_4',
            field=models.CharField(default='2:00 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_5',
            field=models.CharField(default='10:00 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_6',
            field=models.CharField(default='1:30 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_7',
            field=models.CharField(default='11:00 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_8',
            field=models.CharField(default='2:00 PM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_schedule_9',
            field=models.CharField(default='11:00 AM', max_length=20),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_scripture',
            field=models.TextField(default='Scripture for service section'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='service_verse',
            field=models.CharField(default='Act 20:28', max_length=80),
        ),
    ]
