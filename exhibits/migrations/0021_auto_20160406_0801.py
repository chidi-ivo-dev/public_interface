# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0020_exhibit_byline_render_as'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibit',
            old_name='about_exhibit',
            new_name='byline',
        ),
        migrations.RenameField(
            model_name='exhibit',
            old_name='essay',
            new_name='overview',
        ),
    ]
