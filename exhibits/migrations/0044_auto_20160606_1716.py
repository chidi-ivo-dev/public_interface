# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-06 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0043_auto_20160606_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonplan',
            name='lesson_plan',
            field=models.CharField(blank=True, max_length=255, verbose_name='Lesson Plan File URL'),
        ),
    ]
