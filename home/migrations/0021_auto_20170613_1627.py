# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-13 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('home', '0020_regularevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='event_button_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='event_button_text',
            field=models.CharField(default='See more events', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='event_description',
            field=models.TextField(default='Description for Church Event'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='event_main_title',
            field=models.CharField(default='Event', max_length=80),
        ),
        migrations.AddField(
            model_name='homepage',
            name='event_subtitle',
            field=models.CharField(default='Church Event', max_length=100),
        ),
    ]