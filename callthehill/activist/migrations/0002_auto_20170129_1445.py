# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activist',
            name='interests',
            field=models.ManyToManyField(blank=True, to='issues.Tag'),
        ),
    ]
