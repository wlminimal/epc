# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0033_auto_20170613_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='nicaraguapage',
            name='mission_hero_scripture',
            field=models.TextField(default='내가 또 주의 목소리를 들은즉 이르시되 내가 누구를 보내며 누가 우리를 위하여 갈꼬 그 때에 내가 가로되 내가 여기 있나이다 나를 보내소서'),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='mission_hero_title',
            field=models.CharField(default='동부 교회 선교부', max_length=80),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='mission_hero_verse',
            field=models.CharField(default='이사야 6장 8절', max_length=80),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_contact_info',
            field=models.TextField(default='연락처 : nicaragua@epcla.org'),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_content',
            field=wagtail.wagtailcore.fields.RichTextField(default='Intro to English Ministry'),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_content_title_1',
            field=models.CharField(default='니카라과 선교지', max_length=30),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='nicaraguapage',
            name='nicaragua_tab_pastor',
            field=models.CharField(default='선교사 : 김성헌 목사', max_length=50),
        ),
    ]
