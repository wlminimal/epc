# Generated by Django 2.0.7 on 2018-07-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20170710_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lorddayafternoonsermon',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AlterModelOptions(
            name='lorddaymorningsermon',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AlterModelOptions(
            name='philippianssermon',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AlterModelOptions(
            name='psalmssermon',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AlterModelOptions(
            name='revelationsermon',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AlterModelOptions(
            name='romanssermon',
            options={'ordering': ('-upload_date',)},
        ),
        migrations.AddField(
            model_name='lorddayafternoonsermon',
            name='service_date',
            field=models.BigIntegerField(default='2018070911'),
        ),
        migrations.AddField(
            model_name='lorddaymorningsermon',
            name='service_date',
            field=models.BigIntegerField(default='2018070911'),
        ),
        migrations.AddField(
            model_name='philippianssermon',
            name='service_date',
            field=models.BigIntegerField(default='2018070911'),
        ),
        migrations.AddField(
            model_name='psalmssermon',
            name='service_date',
            field=models.BigIntegerField(default='2018070911'),
        ),
        migrations.AddField(
            model_name='revelationsermon',
            name='service_date',
            field=models.BigIntegerField(default='2018070911'),
        ),
        migrations.AddField(
            model_name='romanssermon',
            name='service_date',
            field=models.BigIntegerField(default='2018070911'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type'),
        ),
    ]