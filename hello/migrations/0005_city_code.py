# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-04 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20170927_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='code',
            field=models.CharField(default='BOG', max_length=3),
            preserve_default=False,
        ),
    ]