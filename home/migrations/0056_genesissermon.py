# Generated by Django 2.0.7 on 2018-12-08 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('home', '0055_auto_20180716_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenesisSermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sermon_title', models.TextField(default='Sermon Title')),
                ('sermon_date', models.CharField(default='May 23 2017', max_length=50)),
                ('sermon_chapter', models.CharField(default='Act 22:1-2', max_length=80)),
                ('sermon_link', models.TextField(default='www.youtube.com')),
                ('sermon_share_code', models.CharField(default='LHJowUFSKMA', max_length=80)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('service_date', models.BigIntegerField(default='2018070911')),
                ('sermon_day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.SermonDay')),
                ('sermon_thumbnail_image', models.ForeignKey(help_text='Sermon Thumbnail Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ('-service_date',),
                'abstract': False,
            },
        ),
    ]