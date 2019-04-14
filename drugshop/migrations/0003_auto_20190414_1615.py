# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-14 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drugshop', '0002_auto_20190414_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carret',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drugshop.product'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drugshop.product'),
        ),
    ]
