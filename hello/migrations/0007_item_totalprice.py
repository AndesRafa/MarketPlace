# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_shoppingcart_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='totalPrice',
            field=models.FloatField(default=0),
        ),
    ]