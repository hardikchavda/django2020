# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-11-30 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0003_auto_20201127_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud_info',
            name='s_phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number'),
        ),
    ]
