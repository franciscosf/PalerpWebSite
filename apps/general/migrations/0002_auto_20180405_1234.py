# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-04-05 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posiblecliente',
            name='RUC',
            field=models.CharField(max_length=11),
        ),
    ]
