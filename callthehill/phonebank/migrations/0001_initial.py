# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('issues', '0001_initial'),
        ('activist', '0001_initial'),
        ('legislation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.CharField(choices=[('C', 'Contacted'), ('V', 'Left Voicemail'), ('U', 'Unsuccessful')], max_length=1)),
                ('activist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activist.Activist')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue')),
                ('legislator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislation.Legislator')),
            ],
        ),
    ]