# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baidu_hanyu',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hz', models.CharField(max_length=32)),
                ('py', models.CharField(max_length=32)),
            ],
        ),
    ]
