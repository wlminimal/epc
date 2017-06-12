# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-12 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('home', '0013_auto_20170612_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('blog_hero_title', models.TextField(default='Blog')),
                ('blog_hero_subtitle', models.TextField(default='Subtitle for Blog')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_featured',
            field=models.BooleanField(default=False),
        ),
    ]
