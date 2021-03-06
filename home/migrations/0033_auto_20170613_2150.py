# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0032_auto_20170613_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_content',
            field=wagtail.core.fields.RichTextField(default='Intro to English Ministry'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_content_age',
            field=models.CharField(default='영어가 더 편한, 성인 모든분들을 포함합니다', max_length=50),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_content_info',
            field=models.TextField(default='예배 안내: 오후 1:30 (소예배실)'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_content_title_1',
            field=models.CharField(default='English Ministry', max_length=30),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='em_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_hero_scripture',
            field=models.TextField(default='Scripture for kids page'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_hero_title',
            field=models.CharField(default='English Ministry & 청년부', max_length=80),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_hero_verse',
            field=models.CharField(default='Psalm 119:9-16', max_length=80),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_content',
            field=wagtail.core.fields.RichTextField(default='Intro to 청년부'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_content_age',
            field=models.CharField(default='성인 모든 청년을 대상으로 합니다.', max_length=50),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_content_info',
            field=models.TextField(default='예배 안내: 오후 1:00 청년부실'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_content_title_1',
            field=models.CharField(default='청년부', max_length=30),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='youngadultpage',
            name='ya_tab_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
