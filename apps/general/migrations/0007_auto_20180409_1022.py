# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-04-09 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20180409_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(default='noimagen.jpg', upload_to=''),
        ),
    ]
