# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0031_auto_20170613_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_hero_scripture',
            field=models.TextField(default='Scripture for kids page'),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_hero_title',
            field=models.CharField(default='동부 교회 주일 학교', max_length=80),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_hero_verse',
            field=models.CharField(default='마태복음 18장 2-3절', max_length=80),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_content',
            field=wagtail.core.fields.RichTextField(default='Intro to YG'),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_content_age',
            field=models.CharField(default='6학년부터 12학년까지', max_length=50),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_content_info',
            field=models.TextField(default='예배 안내: 주일 오전 10:30분 성경공부 / 오후 2시 예배 (중고등부실)'),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_content_title_1',
            field=models.CharField(default='중고등부', max_length=30),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youthgrouppage',
            name='yg_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
