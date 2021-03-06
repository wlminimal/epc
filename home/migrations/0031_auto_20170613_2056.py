# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0030_auto_20170613_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_content',
            field=wagtail.core.fields.RichTextField(default='Intro to Elem'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_content_age',
            field=models.CharField(default='0세부터 3세', max_length=50),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_content_info',
            field=models.TextField(default='예배 안내: 오전 11:00 23번 방'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_content_title_1',
            field=models.CharField(default='초등부', max_length=30),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='elem_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kids_hero_scripture',
            field=models.TextField(default='Scripture for kids page'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kids_hero_title',
            field=models.CharField(default='동부 교회 주일 학교', max_length=80),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kids_hero_verse',
            field=models.CharField(default='마태복음 18장 2-3절', max_length=80),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kids_tab_title_1',
            field=models.CharField(default='영아부', max_length=30),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kids_tab_title_2',
            field=models.CharField(default='유치부', max_length=30),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kids_tab_title_3',
            field=models.CharField(default='초등부', max_length=30),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_content',
            field=wagtail.core.fields.RichTextField(default='Intro to Kinder'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_content_age',
            field=models.CharField(default='0세부터 3세', max_length=50),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_content_info',
            field=models.TextField(default='예배 안내: 오전 11:00 23번 방'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_content_title_1',
            field=models.CharField(default='유치부', max_length=30),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='kinder_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_content',
            field=wagtail.core.fields.RichTextField(default='Intro to Nursery'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_content_age',
            field=models.CharField(default='0세부터 3세', max_length=50),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_content_info',
            field=models.TextField(default='예배 안내: 오전 11:00 23번 방'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_content_title_1',
            field=models.CharField(default='영아부', max_length=30),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='kidspage',
            name='nursery_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
