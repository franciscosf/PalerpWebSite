# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-04-07 17:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20180407_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
