# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0042_auto_20160520_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibititem',
            name='custom_metadata',
            field=models.TextField(blank=True, verbose_name='Custom metadata'),
        ),
        migrations.AddField(
            model_name='exhibititem',
            name='metadata_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='item_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='lockup_derivative',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Lockup Image'),
        ),
        migrations.AddField(
            model_name='theme',
            name='sort_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Sortable Title'),
        ),
    ]
