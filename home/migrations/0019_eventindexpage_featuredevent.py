# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0018_remove_blogpage_blog_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('event_hero_title', models.TextField(default='Event')),
                ('event_hero_subtitle', models.TextField(default='Subtitle for Event')),
                ('event_featured_name', models.CharField(default='Featured Event', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FeaturedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(default='Event Title', max_length=50)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.CharField(default='6월 23일', max_length=20)),
                ('event_time', models.CharField(default='11:00 AM', max_length=20)),
                ('event_description', models.TextField(default='Event Description', max_length=150)),
                ('event_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]