# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tardis_portal', '0014_auto_20181002_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='created_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='modified_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]