# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-16 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_auto_20171015_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsperbasket',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='hello.Basket'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='city',
            field=models.CharField(default='Bogota', max_length=150),
        ),
        migrations.AlterField(
            model_name='producer',
            name='typeIdentification',
            field=models.CharField(default='Cedula de Ciudadania', max_length=150),
        ),
    ]
