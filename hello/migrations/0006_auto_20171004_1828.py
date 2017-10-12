# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-10-04 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_city_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='code',
            new_name='shortName',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='AddedDate',
            new_name='addedDate',
        ),
        migrations.RemoveField(
            model_name='product',
            name='catalogue',
        ),
        migrations.AddField(
            model_name='product',
            name='cooperative',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hello.Cooperative'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Catalogue',
        ),
    ]