# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-24 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PosibleCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RUC', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
